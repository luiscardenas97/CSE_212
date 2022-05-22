"""
CSE212 
(c) BYU-Idaho
05-Teach - Problem 1 

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

from ast import Return


def unique_letters(text):
    """ 
    Determine if there are any duplicate letters in the text provided
    """

    # Compare all letters to all other letters
    for i in range(len(text)):  
        for j in range(len(text)):
            if i != j:  # Don't want to compare to yourself ... that will 
                        # always result in a match.
                if text[i] == text[j]:
                    return False
    return True

test1 = "abcdefghjiklmnopqrstuvwxyz"  # Expect True because all letters unique
print(unique_letters(test1))

test2 = "abcdefghjiklanopqrstuvwxyz"  # Expect False because 'a' is repeated
print(unique_letters(test2))

test3 = "" 
print(unique_letters(test3))          # Expect True because its an empty string

def unique_letters_2(text):
    new_set = set()
    for i in range(0, len(text)-1):
        new_list = []
        new_list[:0] = text

        if new_list[i] in new_set:
            return False

        else:
            new_set.add(new_list[i])
    return True
        
            
    

test1 = "abcdefghjiklmnopqrstuvwxyz"  # Expect True because all letters unique
print(unique_letters_2(test1))

test2 = "abcdefghjiklanopqrstuvwxyz"  # Expect False because 'a' is repeated
print(unique_letters_2(test2))

test3 = "" 
print(unique_letters_2(test3))          # Expect True because its an empty string


