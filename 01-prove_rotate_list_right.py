"""
CSE212 
(c) BYU-Idaho
01-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def rotate_list_right(data, amount):
    """
    Rotate the 'data' to the right by the 
    'amount'.   For example, if the data is 
    [1, 2, 3, 4, 5, 6, 7, 8, 9] and an amount
    is 5 then the list returned should be 
    [5, 6, 7, 8, 9, 1, 2, 3, 4].  The value 
    of amount will be in the range of 1 and 
    len(data).
    """
    # It creates a new list in a range from zero to the length of the data
    # It appends in the list the values from the data list but it rotates them to the right by subtracting
    # the amount from the items of the for loop and using that value as the index to get the values 
    # from the data list
    result = [data[x - amount] for x in range(0, len(data))]
    
    return result

print(rotate_list_right([1,2,3,4,5,6,7,8,9],1)) # [9, 1, 2, 3, 4, 5, 6, 7, 8]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],5)) # [5, 6, 7, 8, 9, 1, 2, 3, 4]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],9)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
