
import string

# Class that contains the Binary Search Tree to keep track of Donations
class BST_Donations:
    # Subclass that containts the information for each node. In this case, each node
    # stores the information of donations made by organizations or companies and their names
    class Organization_Donation:
        def __init__(self, data, organization_name):
            self.data = data                                # Donation amount
            self.organization_name = organization_name      # Organization name
            self.larger = None
            self.lower = None

    # Initialize an empty BST
    def __init__(self):
        self.initial = None

    # Insert data to the BST
    def add_donation(self, data, organization_name):
        # If BST is empty, add new node at root.
        if self.initial is None:
            self.initial = BST_Donations.Organization_Donation(data, organization_name)
        # Otherwise, use recursion to find where to add new node
        else:
            self._add_donation(data, organization_name, self.initial)
    
    # Look for the right place where to insert the new node in the BST
    def _add_donation(self, data, organization_name, donation):
        # Check if the new node donation is smaller than the current node donation
        if data < donation.data:
            # If node to the left of current node is empty, add new node there
            if donation.lower is None:
                donation.lower = BST_Donations.Organization_Donation(data, organization_name)
            # Otherwise, use recursion to keep looking for where to add new node
            else:
                self._add_donation(data, organization_name, donation.lower)

        # Check if new node donation is greater than the current node donation
        elif data >= donation.data:
            # If node to the right of the current node is empty, add new node there
            if donation.larger is None:
                donation.larger = BST_Donations.Organization_Donation(data, organization_name)
            # Otherwise, use recursion to keep looking for where to add new node
            else:
                self._add_donation(data, organization_name, donation.larger)

    # Iterator function that will be called each time a 'for' loop is performed
    def __iter__(self):
        yield from self._traverse_forward(self.initial)

    # Allow to traverse forward the BST and return the values of each node from the smallest donation to the largest donation
    def _traverse_forward(self, donation):
        # If current node is not empty, use recursion to return node information
        if donation is not None:
            yield from self._traverse_forward(donation.lower)
            yield donation.data, donation.organization_name
            yield from self._traverse_forward(donation.larger)

    # Perform a backward traversal. It gets called when the method _traverse_backward is called
    def __reversed__(self):
        yield from self._traverse_backward(self.initial)

    # Allow to traverse backward the BST and return the values of each node from the largest donation to the smallest donation
    def _traverse_backward(self, donation):
        # If current node is empty, use recursion to return node information
        if donation is not None:
            yield from self._traverse_backward(donation.larger)
            yield donation.data, donation.organization_name
            yield from self._traverse_backward(donation.lower)

    # Determine if a organization or company already made a donation
    def already_donated(self, organization_name):
        return self._already_donated(organization_name, self.initial)
    
    # Return True whenever a organization or company already made a donation. Otherwise, return False
    def _already_donated(self, organization_name, donation):
        # Check if current node is empty
        if donation is None:
            return False
        # Check if current node is equal to the organization name given
        elif organization_name == donation.organization_name:
            return True
        # When the current node is not equal to the organization name given
        else:
            # If node to the right of current node is empty, perform a recursion to the left
            if donation.larger is None:
                return self._already_donated(organization_name, donation.lower)
            # If node to  the left of the current node is empty, perform a recursion to the right
            elif donation.lower is None:
                return self._already_donated(organization_name, donation.larger)
            # If none of them is empty, perform a recursion to both sides
            else:
                if self._already_donated(organization_name, donation.larger):
                    return True
                elif self._already_donated(organization_name, donation.lower):
                    return True
                else:
                    return False
    
    # Determine the sum of all the donations made
    def total_donation(self):
        if self.initial is None:
            return 0
        else:
            return self._total_donation(self.initial)

    # Return the sum of all the donations made
    def _total_donation(self, donation):
        # If both the node to the right and left of the current node are empty, return the data of current node
        if donation.larger is None and donation.lower is None:
            return donation.data
        
        # If the node to the right of the current node is empty, return data of current node plus the value from recursion to the left
        elif donation.larger is None:
            return donation.data + self._total_donation(donation.lower)
        
        # If the node to the left of the current node is empty, return data of current node plus the value from recursion to the right
        elif donation.lower is None:
            return donation.data + self._total_donation(donation.larger)

        # If none of them are empty, use recursion to the right and left
        else:
            x = donation.data + self._total_donation(donation.larger)
            y = donation.data + self._total_donation(donation.lower)

        # Logic that will avoid to count twice a node
        if x > y:
            y -= donation.data
        else:
            x -= donation.data
        
        # Return sum
        return x + y

# Create an empty BST
donations = BST_Donations()

exit_menu = "no"

# Create menu that allow user to perform different operations with the BST
while exit_menu == "no":
    request = 1
    print("Revenue Restaurant Menu: ")
    print("1) Add donation of a specific organization or company")
    print("2) Display data from largest donation to lowest")
    print("3) Display data from lowest donation to highest")
    print("4) Calculate sum of donations")
    print("5) Exit")
    operation = int(input("\nSelect operation: "))

    # Add new node to the BST. Add new organization or company with its respective donation
    if operation == 1:
        while request == 1:
            organization_name = input("\nPlease enter the name of the organization or company for which you want to add the donation: ")
            organization_name_format = string.capwords(organization_name)
            # Check if a organization or company already made a donation. If they did, print message
            if donations.already_donated(organization_name_format):
                print("\nOrganization or company already made a donation. Please enter another organization or company.")
            # Otherwise, add new organization or company with its respective donation
            else:
                donation_amount = int(input("\nPlease enter the donation amount for that organization or company? "))
                donations.add_donation(donation_amount, organization_name_format)
        
            request = int(input("\nDo you still want to add another organization or company donation? (Enter 1 for yes and 0 for no): "))

    # Print the list with the donations of the whole year in descending order
    elif operation == 2:
        print("\nDonation Amount | Organization or Company")
        for x in reversed(donations):
            print(f"    {x[0]}       |      {x[1]}") 
        print() 

    # Print the list with the donations of the whole year in ascending order
    elif operation == 3:
        print("\nDonation Amount | Organization or Company")
        for x in donations:
            print(f"    {x[0]}       |      {x[1]}") 
        print() 

    # Calculate the sum of total donations made
    elif operation == 4:
        total_donation = donations.total_donation()
        print(f"\nThe total donation during this year is: ${total_donation}")

    # Exit the menu
    elif operation == 5:
        exit_menu = "yes"
    
    print()