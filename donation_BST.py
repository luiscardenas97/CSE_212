
import string

class BST_Donations:
    class Organization_Donation:
        def __init__(self, data, organization_name):
            self.data = data
            self.organization_name = organization_name
            self.larger = None
            self.lower = None

    def __init__(self):
        self.initial = None

    def add_donation(self, data, organization_name):
        if self.initial is None:
            self.initial = BST_Donations.Organization_Donation(data, organization_name)
        else:
            self._add_donation(data, organization_name, self.initial)
    
    def _add_donation(self, data, organization_name, donation):
        if data < donation.data:
            if donation.lower is None:
                donation.lower = BST_Donations.Organization_Donation(data, organization_name)
            else:
                self._add_donation(data, organization_name, donation.lower)

        elif data >= donation.data:
            if donation.larger is None:
                donation.larger = BST_Donations.Organization_Donation(data, organization_name)
            else:
                self._add_donation(data, organization_name, donation.larger)

    def __iter__(self):
        yield from self._traverse_forward(self.initial)

    def _traverse_forward(self, donation):
        if donation is not None:
            yield from self._traverse_forward(donation.lower)
            yield donation.data, donation.organization_name
            yield from self._traverse_forward(donation.larger)

    def __reversed__(self):
        yield from self._traverse_backward(self.initial)

    def _traverse_backward(self, donation):
        if donation is not None:
            yield from self._traverse_backward(donation.larger)
            yield donation.data, donation.organization_name
            yield from self._traverse_backward(donation.lower)

    def already_donated(self, organization_name):
        return self._already_donated(organization_name, self.initial)
    
    def _already_donated(self, organization_name, donation):
        if donation is None:
            return False
        elif organization_name == donation.organization_name:
            return True
        else:
            if donation.larger is None:
                return self._already_donated(organization_name, donation.lower)
            elif donation.lower is None:
                return self._already_donated(organization_name, donation.larger)

            else:
                if self._already_donated(organization_name, donation.larger):
                    return True
                elif self._already_donated(organization_name, donation.lower):
                    return True
                else:
                    return False
    
    def total_donation(self):
        if self.initial is None:
            return 0
        else:
            return self._total_donation(self.initial)

    def _total_donation(self, donation):
        
        if donation.larger is None and donation.lower is None:
            return donation.data
        
        elif donation.larger is None:
            return donation.data + self._total_donation(donation.lower)
        
        elif donation.lower is None:
            return donation.data + self._total_donation(donation.larger)

        else:
            x = donation.data + self._total_donation(donation.larger)
            y = donation.data + self._total_donation(donation.lower)

        if x > y:
            y -= donation.data
        else:
            x -= donation.data
        
        return x + y

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

    # Add new node to the BST. Add new week with its respective revenue
    if operation == 1:
        while request == 1:
            organization_name = input("\nPlease enter the name of the organization or company for which you want to add the donation: ")
            organization_name_format = string.capwords(organization_name)
            if donations.already_donated(organization_name_format):
                print("\nOrganization or company already made a donation. Please enter another organization or company.")
            else:
                donation_amount = int(input("\nPlease enter the donation amount for that organization or company? "))
                donations.add_donation(donation_amount, organization_name_format)
        
            request = int(input("\nDo you still want to add another organization or company donation? (Enter 1 for yes and 0 for no): "))

    # Print the list with the weekly revenues of the whole year in descending order
    elif operation == 2:
        print("\nDonation Amount | Organization or Company")
        for x in reversed(donations):
            print(f"    {x[0]}       |      {x[1]}") 
        print() 

    # Print the list with the weekly revenues of the whole year in ascending order
    elif operation == 3:
        print("\nDonation Amount | Organization or Company")
        for x in donations:
            print(f"    {x[0]}       |      {x[1]}") 
        print() 

    # Calculate the annual profit of the restaurant
    elif operation == 4:
        total_donation = donations.total_donation()
        print(f"\nThe total donation during this year is: ${total_donation}")

    # Exit the menu
    elif operation == 5:
        exit_menu = "yes"
    
    print()