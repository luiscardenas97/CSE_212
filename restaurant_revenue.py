# Class that contains the Binary Search Tree
class BST_Revenue:
    # Subclass that contains the information for each node. In this case, each node
    # store the information of the weekly revenue and week number
    class Biweekly_Revenue:
        def __init__(self, data, week):
            self.data = data            # Weekly revenue
            self.week = week            # Week number
            self.lesser = None
            self.greater = None
    
    # Initialize an empty BST
    def __init__(self):
        self.initial = None
    
    # Insert data to the BST. If the BST is empty, add new node at the root. 
    # Otherwise, use recursion to find where to add new node
    def add_data(self, data, week):
        if self.initial is None:
            self.initial = BST_Revenue.Biweekly_Revenue(data, week) # Insert new node at the root
        else:
            self._add_data(data, week, self.initial)  # Use recursion to find where to insert new node
    
    # Look for the right place where to insert the new node in the BST
    def _add_data(self, data, week, revenue):
        # Check if new node revenue is lesser than the root node revenue
        if data < revenue.data:
            # If node to the left is empty, add new node there
            if revenue.lesser is None:
                revenue.lesser = BST_Revenue.Biweekly_Revenue(data, week)
            # Otherwise, use recursion to keep looking for where to add new node
            else:
                self._add_data(data, week, revenue.lesser)
        
        # Check if new node revenue is greater than the root node revenue
        elif data >= revenue.data:
            # If node to the right is empty, add new node there
            if revenue.greater is None:
                revenue.greater = BST_Revenue.Biweekly_Revenue(data, week)
            # Otherwise, use recursion to keep looking for where to add new node
            else: 
                self._add_data(data, week, revenue.greater)   

    # Iterator function that will be called each time a for loop is performed
    def __iter__(self):
        yield from self._iterate_forward(self.initial)

    # Allow to traverse forward the BST and return the values of each node from
    # lowest revenue to highest revenue
    def _iterate_forward(self, revenue):
        # If root node is not empty, use recursion to return node information
        if revenue is not None:
            yield from self._iterate_forward(revenue.lesser)
            yield [revenue.data, revenue.week]
            yield from self._iterate_forward(revenue.greater)  
    
    # Perform a backward traversal. It gets called when the method _iterate_backward
    # is called.
    def __reversed__(self):
        yield from self._iterate_backward(self.initial)

    # Allow to traverse backward the BST and return the values of each node from
    # highest revenue to lowest revenue
    def _iterate_backward(self, revenue):
        # If root node is not empty, use recursion to return node information
        if revenue is not None:
            yield from self._iterate_backward(revenue.greater)
            yield [revenue.data, revenue.week]
            yield from self._iterate_backward(revenue.lesser) 

    # Determine the sum of the heights of all the subtrees
    def get_amount_of_weeks(self):
        # If root node is empty, return zero
        if self.initial is None:
            return 0
        # Otherwise, use recursion to find the sum of the heights of the subtrees
        else:
            return self._get_amount_of_weeks(self.initial) # Start at the root node

    # Return the sum of the heights of all the subtress
    def _get_amount_of_weeks(self, revenue):
        
        # Check if current node does not have nodes to the right and left
        if revenue.lesser is None and revenue.greater is None:
            return 1
        
        # Check if current node does not have node to the left
        elif revenue.lesser is None:
            return 1 + self._get_amount_of_weeks(revenue.greater)
        
        # Check if current node does not have node to the right
        elif revenue.greater is None:
            return 1 + self._get_amount_of_weeks(revenue.lesser)

        # Current node has nodes to the right and left
        else:
            x =  1 + self._get_amount_of_weeks(revenue.greater)
            y = 1 + self._get_amount_of_weeks(revenue.lesser)
        
        # Avoid counting double some of the nodes
        if x > y:
            y -= 1
        else:
            x -= 1

        return x + y

#Create a new BST
revenue = BST_Revenue()

exit_menu = "no"

# Create menu that allow user to perform different operations with the BST
while exit_menu == "no":
    request = 1
    print("Revenue Restaurant Menu: ")
    print("1) Add revenue of specific week")
    print("2) Display data from highest weekly revenue to lowest")
    print("3) Display data from lowest weekly revenue to highest")
    print("4) Calculate profit")
    print("5) Exit")
    operation = int(input("\nSelect operation: "))

    # Add new node to the BST. Add new week with its respective revenue
    if operation == 1:
        while request == 1:
            week_number = int(input("\nPlease enter the week number for which you want to add the revenue: "))

            revenue_amount = int(input("\nPlease enter the revenue for that week? "))

            revenue.add_data(revenue_amount, week_number)
        
            request = int(input("\nDo you want to add weekly revenue? (Enter 1 for yes and 0 for no): "))

    # Print the list with the weekly revenues of the whole year in descending order
    elif operation == 2:
        print("Weekly Revenue | Week Number")
        for x in reversed(revenue):
            print(f"    {x[0]}       |    {x[1]}") 
        print() 

    # Print the list with the weekly revenues of the whole year in ascending order
    elif operation == 3:
        print("\nWeekly Revenue | Week Number")
        for x in revenue:
            print(f"    {x[0]}       |    {x[1]}") 
        print() 

    # Calculate the annual profit of the restaurant
    elif operation == 4:
        amount_week = revenue.get_amount_of_weeks()
        fixed_cost = 5000
        total_revenue = 0
        for x in revenue:
            total_revenue += x[0]
        total_profit = total_revenue - (5000 * amount_week)
        print(f"\nThe total profit for your restaurant during this year is: ${total_profit}")

    # Exit the menu
    elif operation == 5:
        exit_menu = "yes"
    
    print()
