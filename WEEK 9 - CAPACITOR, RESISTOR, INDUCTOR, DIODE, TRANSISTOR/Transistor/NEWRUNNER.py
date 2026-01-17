'''
def print_student_info(name, grade, course):
    print(f"{name} | grade: {grade} | course: {course}")

student1_name = "Johen"
student1_grade = 1.2
student1_course = ["Chem 015", "Physics 2"]

student2_name = "Jay"
student2_grade = 1.4
student2_course = ["Chem 015", "Physics 2"]

student3_name = "Diego"
student3_grade = 1.7
student3_course = ["Chem 015", "Physics 2"]

print_student_info(student1_name, student1_grade, student1_course)
print_student_info(student2_name, student2_grade, student2_course)
print_student_info(student3_name, student3_grade, student3_course)

class Student:
    def __init__(self, name, grade, course):
        self.name = name
        self.grade = grade
        self.course = course

    def print_student_info(self):
        print(f"{self.name} grade: {self.grade} course: {self.course}")


student1 = Student("Spongebob", "1.1", ["Chem 015", "Physics 2"])
student2 = Student("Patrick", "1.4", ["Biology 1", "Math 2"])
student3 = Student("Squidward", "1.7", ["Physics 2", "Art Appreciation"])

student1.print_student_info()
student2.print_student_info()
student3.print_student_info()

import NEWRUNNER

student1 = NEWRUNNER.Student(
    name="Spongebob",
    grade="1.1",
    course=["Chem 015", "Physics 2"]
)

student1.print_student_info()

class Student:
    def __init__(self, name, grade, subjects):
        self.name = name
        self.grade = float(grade)
        self.subjects = subjects

    def is_grade_passing(self):
        return self.grade <= 3.0

    def print_student_info(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Subjects: {', '.join(self.subjects)}")
        print(f"Passing: {'Yes' if self.is_grade_passing() else 'No'}")
        print("-" * 30)


student1 = Student("Spongebob", "1.1", ["Chem 015", "Physics 2"])
student2 = Student("Patrick", "1.4", ["Biology 1", "Math 2"])
student3 = Student("Squidward", "5.0", ["Physics 2", "Art Appreciation"])

student1.print_student_info()
student2.print_student_info()
student3.print_student_info()


class Student:
    def __init__(self, name, grade, subjects):
        self.name = name
        self.grade = float(grade)
        self.subjects = subjects

    def is_grade_passing(self):
        return self.grade <= 3.0

    @staticmethod
    def print_student_info(student):
        print(f"Name: {student.name}")
        print(f"Grade: {student.grade}")
        print(f"Subjects: {', '.join(student.subjects)}")

        if student.is_grade_passing():
            print("Passing: Yes. Keep up the good work!")
        else:
            print("Passing: No. Focus on improvement.")

        print("-" * 40)


student1 = Student("Spongebob", "1.1", ["Chem 015", "Physics 2"])
student2 = Student("Patrick", "1.4", ["Biology 1", "Math 2"])
student3 = Student("Squidward", "5.0", ["Physics 2", "Art Appreciation"])


class Student:
    all_students = []

    def __init__(self, name, grade, subjects):
        self.name = name
        self.grade = float(grade)
        self.subjects = subjects
        Student.all_students.append(self)

    def is_grade_passing(self):
        return self.grade <= 3.0

    @classmethod
    def print_all_students_info(cls):
        for student in cls.all_students:
            print(f"Name: {student.name}")
            print(f"Grade: {student.grade}")
            print(f"Subjects: {', '.join(student.subjects)}")

            if student.is_grade_passing():
                print("Passing: Yes. Woah")
            else:
                print("Passing: Nope. Failed")

            print("-" * 40)
        return cls


student1 = Student("Spongebob", "1.1", ["Chem 015", "Physics 2"])
student2 = Student("Patrick", "1.4", ["Biology 1", "Math 2"])
student3 = Student("Squidward", "5.0", ["Physics 2", "Art Appreciation"])

Student.print_all_students_info()
'''

