

def say_hello(count):
	if count <= 0:  # Base Case
		return
	else:
		print("Hello")
		say_hello(count-1)  # Smaller Problem

def factorial(n):
	if n <= 1:
		return 1  # 1! = 1 (no recursion)
	else:
		return n * factorial(n-1)  # n! = n * (n-1)!

def fib(n):
	if n <= 2:   
		return 1    # fib(2) = 1 and fib(1) = 1
	else:
		return fib(n-1) + fib(n-2)  # fib(n) = fib(n-1) + fib(n-2)

def fibonacci(n, remember = None):
    # If this is the first time calling the function, then
    # we need to create the dictionary.
    if remember is None:
        remember = dict()

    # Base Case
    if n <= 2:
        return 1

    # Check if we have solved this one before
    if n in remember:
        return remember[n]

    # Otherwise solve with recursion
    result = fibonacci(n-1, remember) + fibonacci(n-2, remember)

    # Remember result for potential later use
    remember[n] = result
    return result

print(fibonacci(1))    # 1
print(fibonacci(2))    # 1
print(fibonacci(3))    # 2
print(fibonacci(4))    # 3
print(fibonacci(10))   # 55
print(fibonacci(100))  # 354224848179261915075 (This one will
                       # not work if you don't have the 
                       # 'remember' dictionary implemented).

say_hello(5)
print(factorial(10))
print(fib(9))



def permutations(letters, word=""):

	if len(letters) == 0:   # Base Case
		print(word)  

	else:
		# Try adding each of the available letters
		# to the 'word_so_far' and add up all the
		# resulting permutations.

		for index in range(len(letters)):
			# Make a copy of the letters to pass to the
			# the next call to permutations.  We need
			# to remove the letter we just added before
			# we call permutations again.

			letters_left = letters[:]
			del letters_left[index]

			# Add the new letter to the word we have so far
			permutations(letters_left, word + letters[index])

permutations(list("ABC"))
""" 
Results:
ABC
ACB
BAC
BCA
CAB
CBA
"""

permutations(list("ABCD"))
"""
Results:
ABCD
ABDC
ACBD
ACDB
ADBC
ADCB
BACD
BADC
BCAD
BCDA
BDAC
BDCA
CABD
CADB
CBAD
CBDA
CDAB
CDBA
DABC
DACB
DBAC
DBCA
DCAB
DCBA
"""

def binary_search(sorted_list, target):
    """
    This function uses list slicing.  A list slice will create a list from another list
    This is useful when we want to create new sublists.  Here is how list slicing works:
    
    data[:a] - Creates a new list from index 0 to index a-1
    data[a:] - Creates a new list from index a to len(data)-1
    data[a:b] - Creates a new list from index a to index b-1
    data[a:b:c] - Creates a new list from index a to index b-1 stepping by c
    """
    if len(sorted_list) == 1:  
        # Base Case
        return target == sorted_list[0]
    else:
        # Find the middle and compare
        middle = len(sorted_list) // 2
        if target == sorted_list[middle]:
            # We got lucky and the middle was the match
            return True
        elif target < sorted_list[middle]:
            # Search the first half (index 0 to middle-1) and 
            # return the result
            return binary_search(sorted_list[:middle],target)
        else:
            # Search the second half (index middle to end) and 
            # return the result
            return binary_search(sorted_list[middle:],target)

print(binary_search([1, 3, 6, 18, 20, 25, 34, 38, 89, 95, 99, 100], 89)) # True
print(binary_search([1, 3, 6, 18, 20, 25, 34, 38, 89, 95, 99, 100], 1))  # True
print(binary_search([1, 3, 6, 18, 20, 25, 34, 38, 89, 95, 99, 100], 17)) # False