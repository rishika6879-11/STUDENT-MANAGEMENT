'''
Project: Student Management System
Problem Statement

Create a Student Management System using Python and Object-Oriented Programming (OOP).

The system should allow the user to:

Add a new student.
View all students.
Search for a student using Student ID.
Update a student's marks.
Delete a student record using Student ID.
Display the student with the highest marks.
Exit the application.
Student Details

Each student should have:

Student ID
Student Name
Age
Marks
'''

class Student:
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name} ")
        print(f"Age: {self.age}") 
        print(f"Marks: {self.marks}")

class studentmanagementsystem:
    def __init__(self):
        self.students=[]
        
    def add_students(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))
        
        student = Student(student_id, name, age, marks)
        self.students.append(student)
        print('Student detail added successfully')
        
    def display_student(self):
        if len(self.students) == 0:
            print("Students not found")
            return
        for student in self.students:
            student.display()   
                
    def search_student(self):
        student_id = input("Enter Student ID to search: ")
        for student in self.students:
            if student.student_id==student_id:
                print("found the record of the student")
                student.display()
                return
        print("no student found")
                
    def update_marks(self):
        student_id = input("Enter Student ID to update marks: ")
        for student in self.students:
            if student.student_id==student_id:
                print(f"Current Record: Name: {student.name} | Marks: {student.marks}")
                new_marks=float(input("enter the new marks: "))
                student.marks=new_marks
                print(" Marks updated successfully!")
                student.display()
                return
        print("no student found: ")
    
    
    def delete_student(self):
        student_id = input("Enter Student ID to delete details: ")
        for student in self.students:
            if student.student_id==student_id:
                self.students.remove(student)
                print(f" Success: Record for '{student.name}' has been deleted.")
                return
        print(" Student ID not found.")
                
    def display_highest_marks(self):
        if len(self.students)==0:
                print("no record found")
                return
        highest_student=self.students[0]
        for student in self.students:
            if student.marks > highest_student.marks:
                highest_student = student  
        print(" Top Performing Student:")
        highest_student.display()   
        
            
            
            
def main():
    s=studentmanagementsystem()
    
    while True:
        print("\n==============================")
        print("📘 STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add a New Student")
        print("2. View All Students")
        print("3. Search for a Student")
        print("4. Update a Student's Marks")
        print("5. Delete a Student Record")
        print("6. Display Student with Highest Marks")
        print("7. Exit Application")
        print("==============================")
        
        choice = input("Select an option (1-7): ")
        
        if choice == '1':
            s.add_students()
        elif choice == '2':
            s.display_student()
        elif choice == '3':
            s.search_student()
        elif choice == '4':
            s.update_marks()
        elif choice == '5':
            s.delete_student()
        elif choice == '6':
            s.display_highest_marks()
        elif choice == '7':
            print("\n Exiting the application. Goodbye!")
            break
        else:
            print(" Invalid selection! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()




        
        


    

        



