import re
import json
import csv
import xml.etree.ElementTree as Element_tree
# function to check lines


def line_handler(count_lines, file, id_term):
    for line in file:
        count_lines += 1

        if id_term in line:
            print("logged in user:", line)

            # validating password

            user_password = password_validate()

            # submit handler
            submit_handler(user_password, line)


# function to validate password


def password_validate():
    count_trial = 3
    while True and count_trial > 0:
        password = input("Enter a password: ")
        special_char_check = re.compile('[@_#$%^&*()<>?/|}{~:]')
        reserved_char_check = re.compile('[!,+=]')

        if len(password) < 8:
            count_trial -= 1
            print("Make sure your password is at lest 8 letters ({0} trials left!!)".format(count_trial))

        elif not  any(character.isalnum() for character in password):
            count_trial -= 1
            print("Password should atleast contain a special character in it ({0} trials left!!)".format(count_trial))

        elif reserved_char_check.search(password) != None:
            count_trial -= 1
            print("Password should not contain a reserved character in it ({0} trials left!!)".format(count_trial))

        elif re.search('[a-z]', password) is None:
            count_trial -= 1
            print("Make sure your password has a lower letter in it ({0} trials left!!)".format(count_trial))

        elif not any(character.isupper() for character in password):
            count_trial -= 1
            print("Make sure your password has a capital letter in it ({0} trials left!!)".format(count_trial))

        elif re.search('[0-9]', password) is None:
            count_trial -= 1
            print("Make sure your password has a number in it ({0} trials left!!)".format(count_trial))

        else:
            return password


# function to submit password


def submit_handler(user_password, line):
    if user_password != None:

        password_term = ", password:" + user_password

        for each_character in password_term:
            line = line.rstrip() + each_character
        print("updated user: " + line)
        print(updated_students("final_students.txt", "a", line))

    else:
        print("Invalid password")


# function to update the student


def updated_students(file_destination, file_option, student):
    new_students = []
    new_students.append(student)
    new_file = open(file_destination, file_option)

    for student in new_students:
        new_file.write(student + '\n')
    new_file.close()
    return True

# function to check if the student is already updated


def check_updated_students(line_to_check):
    file = open("final_students.txt", "r")

    for lines in file:
        if line_to_check not in lines:
            return True

        elif line_to_check in lines:
            return False
    file.close()
