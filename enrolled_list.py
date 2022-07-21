
import string

class EnrolledList:
    class Student_Name:
        def __init__(self, student_name):
            self.student_name = student_name
            self.next_student = None
            self.previous_student = None
    
    def __init__(self):
        self.first_student = None
        self.last_student = None

    def insert_student__at_front(self, student_name):
        new_student = EnrolledList.Student_Name(student_name)

        if self.first_student is None:
            self.first_student = new_student
            self.last_student = new_student

        else:
            new_student.next_student = self.first_student
            self.first_student.previous_student = new_student
            self.first_student = new_student

    def insert_student_at_end(self, student_name):
        new_student = EnrolledList.Student_Name(student_name)

        if self.first_student is None:
            self.first_student = new_student
            self.last_student = new_student

        else:
            new_student.previous_student = self.last_student
            self.last_student.next_student = new_student
            self.last_student = new_student

    def insert_student_after(self, student_name, enrolling_student):
        current_student = self.first_student
        while current_student is not None:
            if current_student.student_name == student_name:
                if current_student == self.last_student:
                    self.insert_student_at_end(enrolling_student)
                else:
                    new_student = EnrolledList.Student_Name(enrolling_student)
                    new_student.previous_student = current_student
                    new_student.next_student = current_student.next_student
                    current_student.next_student.previous_student = new_student
                    current_student.next_student = new_student
            
            current_student = current_student.next_student

    def remove_student_at_front(self):
        if self.first_student == self.last_student:
            self.first_student = None
            self.last_student = None
        elif self.first_student is not None:
            self.first_student.next_student.previous_student = None
            self.first_student = self.first_student.next_student

    def remove_student_at_end(self):
        if self.first_student == self.last_student:
            self.first_student = None
            self.last_student = None
        elif self.last_student is not None:
            self.last_student.previous_student.next_student = None
            self.last_student = self.last_student.previous_student

    def remove_student_in_middle(self, student_name):
        current_student = self.first_student
        while current_student is not None:
            if current_student.student_name == student_name:
                if current_student.student_name == self.first_student.student_name:
                    self.remove_student_at_front()
                elif current_student.student_name == self.last_student.student_name:
                    self.remove_student_at_end()
                elif current_student.student_name != self.first_student.student_name:
                    current_student.next_student.previous_student = current_student.previous_student
                    current_student.previous_student.next_student = current_student.next_student
                return
            current_student = current_student.next_student
        if current_student == None and current_student.student_name == student_name:
            print("We're sorry, but you can remove the student. The list is empty.")

    def __iter__(self):
        
        current_student = self.first_student
        while current_student is not None:
            yield current_student.student_name
            current_student = current_student.next_student

    def __str__(self):
        student_list = "Enrolled Students for Circuits Class: \n"
        for student in self:
            student_list += student
            student_list += "\n"
        
        return student_list

student_list = EnrolledList()

exit_menu = "no"

while exit_menu == "no":
    request = 1
    print("Enrolled List Menu: ")
    print("1) Add student to enrolled list at beginning or end of the list")
    print("2) Add student to enrolled list after an specific student")
    print("3) Remove student from enrolled list")
    print("4) Print list of students enrolled in the course")
    print("5) Exit")
    operation = int(input("\nSelect operation: "))

    if operation == 1:
        while request == 1:
            student_name = input("\nPlease introduce the name of the new student you want to add to the enrolled list: ")
            student_name_format = string.capwords(student_name)
            order = input("\nDo you want to add new student at the beginning or end of the list (Enter 1 for beginning or 0 for end)? ")
            if order == 1:
                student_list.insert_student__at_front(student_name_format)
            else:
                student_list.insert_student_at_end(student_name_format)
            
            request = int(input("\nDo you want to add another student at the beginning or end of the enrolled list? (Enter 1 for yes and 0 for no): "))

    elif operation == 2:
        while request == 1:
            student_name = input("\nPlease introduce the name of the new student you want to add to the enrolled list: ")
            student_name_format = string.capwords(student_name)
            previous_student = input("\nPlease introduce the name of the student after which you want to add the new student: ")
            previous_student_format = string.capwords(previous_student)
            student_list.insert_student_after(previous_student_format, student_name_format)

            request = int(input("\nDo you want to add another student at the middle of the enrolled list? (Enter 1 for yes and 0 for no): "))

    elif operation == 3:
        while request == 1:
            student_name = input("\nPlease introduce the name of the student you want remove from the enrolled list: ")
            student_name_format = string.capwords(student_name)
            student_list.remove_student_in_middle(student_name_format)

            request = int(input("\nDo you want to remove another student from the enrolled list? (Enter 1 for yes and 0 for no): "))
    
    elif operation == 4:
        print()
        print(student_list)

    elif operation == 5:
        exit_menu = "yes"
    
    print()


