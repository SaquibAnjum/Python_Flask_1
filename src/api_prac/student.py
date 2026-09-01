class Student:

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"

    def get_details(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
            "grade": self.calculate_grade()
        }

    def update_marks(self, marks):
        self.marks = marks


class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def update_student(self, student_id, data):
        student = self.find_student(student_id)

        if student is None:
            return None

        if "name" in data:
            student.name = data["name"]

        if "age" in data:
            student.age = data["age"]

        if "course" in data:
            student.course = data["course"]

        if "marks" in data:
            student.update_marks(data["marks"])

        return student

    def delete_student(self, student_id):
        student = self.find_student(student_id)

        if student is None:
            return False

        self.students.remove(student)
        return True

    def get_all_students(self):
        return self.students

    def get_passed_students(self):
        return [
            student
            for student in self.students
            if student.marks >= 40
        ]

    def get_stats(self):
        if not self.students:
            return {
                "total_students": 0,
                "average_marks": 0,
                "highest_marks": 0,
                "lowest_marks": 0
            }

        marks = [student.marks for student in self.students]

        return {
            "total_students": len(self.students),
            "average_marks": round(sum(marks) / len(marks), 2),
            "highest_marks": max(marks),
            "lowest_marks": min(marks)
        }