
import string

# Create class that will contain the linked list
class EnrolledList:
    # Create class that will contain each student name as a node
    class Student_Name:
        def __init__(self, student_name):
            self.student_name = student_name
            self.next_student = None
            self.previous_student = None
    
    # Create a empty linked list
    def __init__(self):
        self.first_student = None
        self.last_student = None

    # Method that allows the user add a new student at the beginning of the list
    def insert_student__at_front(self, student_name):
        new_student = EnrolledList.Student_Name(student_name)

        # If linked list is empty, add new student at the beginning of the list
        if self.first_student is None:
            self.first_student = new_student
            self.last_student = new_student

        # Otherwise, add new student at the beginning of the link by making old first student, the second student in the list
        else:
            new_student.next_student = self.first_student
            self.first_student.previous_student = new_student
            self.first_student = new_student

    # Method that allows the user add a new student at the end of the list
    def insert_student_at_end(self, student_name):
        new_student = EnrolledList.Student_Name(student_name)

        # If linked list is empty, add new student at the end of the list
        if self.first_student is None:
            self.first_student = new_student
            self.last_student = new_student

        # Otherwise, add new student at the end of the link by making old last student, the second to last student in the list
        else:
            new_student.previous_student = self.last_student
            self.last_student.next_student = new_student
            self.last_student = new_student

    # Method that allows the user add a new student after another student
    def insert_student_after(self, student_name, enrolling_student):
        # Starting from the first student in the linked list, loop through each student until it finds the student after which new student will be added
        current_student = self.first_student
        # If linked list is not empty, keep looping through the list
        while current_student is not None:
            # Check if the current student in the list is the same as the student after which the new student will be added. If it's, add new student after the current student
            if current_student.student_name == student_name:
                # If current student is the same as the last student, add new student at the end of the linked list
                if current_student.student_name == self.last_student.student_name:
                    self.insert_student_at_end(enrolling_student)
                # Add new student after the current student
                else:
                    new_student = EnrolledList.Student_Name(enrolling_student)
                    new_student.previous_student = current_student
                    new_student.next_student = current_student.next_student
                    current_student.next_student.previous_student = new_student
                    current_student.next_student = new_student
            
            # Go to next student in the list 
            current_student = current_student.next_student

    # Method that allows the user remove a student from the linked list at the beginning of the list
    def remove_student_at_front(self):
        # If there is only one student in the linked list, remove that student
        if self.first_student.student_name == self.last_student.student_name:
            self.first_student = None
            self.last_student = None
        # As long as the linked list is not empty, remove student at the beginning of the list
        elif self.first_student is not None:
            self.first_student.next_student.previous_student = None
            self.first_student = self.first_student.next_student

    # Method that allows the user remove a student from the linked list at the end of the list
    def remove_student_at_end(self):
        # If there is only one student in the linked list, remove that student
        if self.first_student.student_name == self.last_student.student_name:
            self.first_student = None
            self.last_student = None
        # As long as there is a last student, remove student at the beginning of the list
        elif self.last_student is not None:
            self.last_student.previous_student.next_student = None
            self.last_student = self.last_student.previous_student

    # Method that allows the user remove a student from the linked list at the middle of the list
    def remove_student_in_middle(self, student_name):
        # Starting from the first student in the linked list, loop through each student until it finds the student that will be removed
        current_student = self.first_student
        # If linked list is not empty, keep looping through the list
        while current_student is not None:
            # Check if the current student in the list is the same as the student that will be remove. If it's, remove the student
            if current_student.student_name == student_name:
                # If current student is the first one in the list, remove that student
                if current_student.student_name == self.first_student.student_name:
                    self.remove_student_at_front()
                # If current student is the last one in the list, remove that student
                elif current_student.student_name == self.last_student.student_name:
                    self.remove_student_at_end()
                # As long as the current student is not the same as the first student, remove that student
                elif current_student.student_name != self.first_student.student_name:
                    current_student.next_student.previous_student = current_student.previous_student
                    current_student.previous_student.next_student = current_student.next_student
                return
            
            # Go to next student
            current_student = current_student.next_student
        
        # If linked list is empty, print message
        if current_student == None:
            print("We're sorry, but you can remove the student. The list is empty.")

    # Iterate through the linked list. Allow the user to use 'for' loop
    def __iter__(self):
        # Starting from the first student in the linked list, iterate through each student in the list
        current_student = self.first_student
        # As long as the end of the list is not reached, keep looping
        while current_student is not None:
            # Return the name of the current student
            yield current_student.student_name
            # Go to next student
            current_student = current_student.next_student
    
    # Method that checks if a student name is already in the linked list
    def is_in_list(self, student_name):
        # Starting from the first student in the linked list, iterate through each student in the list
        current_student = self.first_student
        # As long as the end of the list is not reached, keep looping
        while current_student is not None:
            # Check if current student in the iteration is equal to the student name. If it's, return True
            if current_student.student_name == student_name:
                return True
            # Go to next student
            current_student = current_student.next_student
        # Otherwise, return False
        return False

    # Method that allow to print the student in the linked list as string
    def __str__(self):
        student_list = "Enrolled Students for Circuits Class: \n"
        for student in self:
            student_list += student
            student_list += "\n"
        
        return student_list

student_list = EnrolledList()

exit_menu = "no"

# Create menu that allow user to perform different operations with the linked list
while exit_menu == "no":
    request = 1
    print("Enrolled List Menu: ")
    print("1) Add student to enrolled list at beginning or end of the list")
    print("2) Add student to enrolled list after an specific student")
    print("3) Remove student from enrolled list")
    print("4) Print list of students enrolled in the course")
    print("5) Exit")
    operation = int(input("\nSelect operation: "))

    # Add new student at the beginning or end of the linked list
    if operation == 1:
        while request == 1:
            student_name = input("\nPlease introduce the name of the new student you want to add to the enrolled list: ")
            student_name_format = string.capwords(student_name)
            #If name is already in the list, don't add the name
            if student_list.is_in_list(student_name_format):
                print("\nStudent is already in the list. Please add another student.")
            #If name is not in the list, add the name
            else:
                order = int(input("\nDo you want to add new student at the beginning or end of the list (Enter 1 for beginning or 0 for end)? "))
                if order == 1:
                    student_list.insert_student__at_front(student_name_format)
                else:
                    student_list.insert_student_at_end(student_name_format)
            
            request = int(input("\nDo you still want to add another student at the beginning or end of the enrolled list? (Enter 1 for yes and 0 for no): "))

    # Add new student to the linked list after an specific student
    elif operation == 2:
        while request == 1:
            student_name = input("\nPlease introduce the name of the new student you want to add to the enrolled list: ")
            student_name_format = string.capwords(student_name)
            #If name is already in the list, don't add the name
            if student_list.is_in_list(student_name_format):
                print("\nStudent is already in the list. Please add another student.")
            #If name is not in the list, add the name
            else:
                previous_student = input("\nPlease introduce the name of the student after which you want to add the new student: ")
                previous_student_format = string.capwords(previous_student)
                student_list.insert_student_after(previous_student_format, student_name_format)

            request = int(input("\nDo you still want to add another student at the middle of the enrolled list? (Enter 1 for yes and 0 for no): "))

    # Remove student from linked list
    elif operation == 3:
        while request == 1:
            student_name = input("\nPlease introduce the name of the student you want to remove from the enrolled list: ")
            student_name_format = string.capwords(student_name)
            student_list.remove_student_in_middle(student_name_format)

            request = int(input("\nDo you want to remove another student from the enrolled list? (Enter 1 for yes and 0 for no): "))
    
    # Print linked list
    elif operation == 4:
        print()
        print(student_list)

    # Exit the menu
    elif operation == 5:
        exit_menu = "yes"
    
    print()


