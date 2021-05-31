class Student:
    def __init__(self, students, lines, student_list):
        self.students = students
        self.lines = lines
        self.student_list = student_list

    def serialize(self, serializer):
        serializer.serialize_object(self.students, self.lines, self.student_list)
