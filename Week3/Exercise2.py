import random
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import Exercise1 as ex1

# 1) Create a function that can take a list of students and return the 3 students closest to completing their study.
# 2) If list is shorter than 3 raise your own custom exception(NotEnoughStudentsException)
# 3) Create another function that can create a csv file with 3 students closest to completion
# A) If an exception is raised write an appropriate message to the file

week3_path = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week3\\'
csv_students = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week3\\students.csv'


class NotEnoughStudentsException(Exception):
    pass


class TooManyStudentsException(Exception):
    pass


def closests_to_completetion(students, desc):
    if len(students) < 3:
        raise NotEnoughStudentsException(
            'Fewer than 3 students in list: students')
    students3 = []
    students_sorted = sorted(
        students, key=lambda student: student.completed_courses(), reverse=desc)
    for i in range(3):
        students3.append(students_sorted[i])
    return students3


def write_students_to_file(outputpath, students: []):
    try:
        if len(students) > 3:
            raise TooManyStudentsException(
                'Yoo many students in list: students')
        else:
            with open(outputpath+'students3.csv', 'w', newline='') as csv_output:
                csvwriter = csv.writer(csv_output)
                header = ['Name', 'ects-completed', 'avg-grade']
                csvwriter.writerow(header)
                for student in students:
                    csvwriter.writerow(
                        [student.name, str(student.completed_courses()), str(student.get_avg_grade())])
    except Exception as e:
        print(e)
        with open(outputpath+'students3.csv', 'w', newline='') as csv_output:
            csvwriter = csv.writer(csv_output)
            csvwriter.writerow([str(e)])


# if __name__ == "__main__":
    # closests_to_completetion(ex1.read_students_to_list(csv_students), True)
    # write_students_to_file(week3_path, closests_to_completetion(ex1.read_students_to_list(csv_students), True))
