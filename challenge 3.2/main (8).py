def sort_students(students):
    sorted_students = sorted(students, key=lambda student: student.cgpa, reverse=True)
    return sorted_students
class Student:
    def _init_(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

students = [
    Student("Alice", "A001", 3.8),
    Student("Bob", "B002", 3.5),
    Student("Charlie", "C003", 3.9),
    Student("David", "D004", 3.7),
]

sorted_students = sort_students(students)
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")