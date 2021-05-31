import student
import json
import xml.etree.ElementTree as Element_tree
import socket
import csv

# function to update the student

HOST = '127.0.0.1'
PORT = 11122


def updated_students(file_destination, file_option, student):
    new_students = []
    new_students.append(student)
    new_file = open(file_destination, file_option)

    for student in new_students:
        new_file.write(student + '\n')
    new_file.close()
    return True


class JsonSerializer:
            def __init__(self):
                self._current_object = None

            def serialize_object(self, students, lines, student_list):

                for line in lines:
                    students_dict = {}
                    one_line = line.rstrip().split(',')
                    for each_element in one_line:
                        splitted_element = each_element.split(':')
                        students_dict.update({splitted_element[0]: splitted_element[1]})
                    student_list.append(students_dict)
                export_file = json.dumps(student_list, indent=4)
                updated_students("final_students.json", "w", str(export_file))

                # print("New Saved Student: " + str(json.dumps(student_list)))
                students.close()

                self._current_object = export_file

            def export(self):
                return self._current_object.encode(encoding="UTF-8")


class CsvSerializer:
    def __init__(self):
        self._current_object = None

    def serialize_object(self, students, lines, student_list):

        student_csv = open("final_students.csv", "w")
        export_to_csv = csv.writer(student_csv, delimiter=',')
        export_to_csv.writerow(('id', 'firstname', 'lastname', 'password'))
        final_string = ''
        export_file = ''

        for each_line in lines:
            split_el = each_line.strip().split(',')
            for each_splitted_el in split_el:
                final_string += each_splitted_el.split(':')[1] + ','
        export_file = final_string[:-1] + '\n'
        print(export_file)
            # student_csv.write(final_string[:-1] + '\n')
        # print("a CSV file has been created")
        students.close()
        self._current_object = export_file

    def export(self):
        return self._current_object.encode(encoding="UTF-8")

# failed to send xml to the server as an encoded text, still working on it

class XmlSerializer:
    def __init__(self):
        self._current_object = None

    def serialize_object(self, students, lines, student_list):

        student = Element_tree.Element("student")

        for each_student in range(len(lines)):
            student_el = Element_tree.SubElement(student, "data")
            student_el.text = str(lines[each_student]) + ' '

        student_tree = Element_tree.ElementTree(student)
        student_tree.write("final_students.xml", encoding='utf-8', xml_declaration=True)
        # print("an XML file has been created")
        self._current_object = ''.encode(encoding="UTF-8")
        students.close()


    def export(self):
        return self._current_object


class SerializerFactory:
    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            print('no creator found')
            raise ValueError(format)
        return creator()


factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('CSV', CsvSerializer)
factory.register_format('XML', XmlSerializer)

class ObjectSerializer:
    def serialize(self, student, format):
        serializer = factory.get_serializer(format)
        student.serialize(serializer)
        return serializer.export()



students = open("final_students.txt", "r")
lines = students.readlines()
student_list = []

user_preference = input("Choose a preferred format(JSON, CSV, XML): ")

student = student.Student(students, lines, student_list)

final_output = ObjectSerializer().serialize(student, user_preference.upper())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(final_output)
