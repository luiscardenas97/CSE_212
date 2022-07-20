
from calendar import c
from turtle import st

from urllib3 import Retry


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
                    new_student = EnrolledList.Student_Name(student_name)
                    new_student.previous_student = current_student
                    new_student.next_student = current_student.next_student
                    current_student.next_student.previous_student = new_student
                    current_student.next_student = new_student
            
            current_student = current_student.next_student

    def remove_student_at_front(self):
        self.first_student.next_student.previous_student = None
        self.first_student = self.first_student.next_student

    def remove_student_at_end(self):
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

    def __iter__(self):
        
        current_student = self.first_student
        while current_student is not None:
            yield current_student.student_name
            current_student = current_student.next_student

    def __str__(self):
        student_list = ""
        for student in self:
            student_list += student
            student_list += "\n"
        
        return student_list

student_list = EnrolledList()
student_list.insert_student__at_front("Luis Roberto Cardenas")
student_list.insert_student_after("Luis Roberto Cardenas","Sarah Cardenas")
student_list.insert_student_at_end("Luna Cardenas")
print(student_list)
print()
student_list.remove_student_in_middle("Sarah Cardenas")
print(student_list)


