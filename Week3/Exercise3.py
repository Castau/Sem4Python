import random
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import Exercise1 as ex1
import Exercise2 as ex2

# 1) Create a function that can take a list of students and show a pie chart of how students are distributed in ECTS percentage categories (10 %, 20%, ...)
# 2) create a function that can take a list of students and show how many students have taken each course(bar chart)
# A) create a method on student that can return a list of courses
# 3) make the figure show males and females in different colors for each course(display 2 datasets in same figure)

week3_path = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week3\\'
csv_students = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week3\\students.csv'


def student_completion_piechart(studcomp):
    fig1, ax1 = plt.subplots()
    ax1.pie(studcomp.values(), explode=None, labels=studcomp.keys(), autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()


# ['Abjuration', 'Conjuration', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation']

def students_per_course(students):
    studcompMale = {}
    studcompMale['Abjuration'] = 0
    studcompMale['Conjuration'] = 0
    studcompMale['Evocation'] = 0
    studcompMale['Illusion'] = 0
    studcompMale['Necromancy'] = 0
    studcompMale['Transmutation'] = 0

    studcompFemale = {}
    studcompFemale['Abjuration'] = 0
    studcompFemale['Conjuration'] = 0
    studcompFemale['Evocation'] = 0
    studcompFemale['Illusion'] = 0
    studcompFemale['Necromancy'] = 0
    studcompFemale['Transmutation'] = 0

    for student in students:
        for course in student.get_courses():
            if course.name == 'Abjuration':
                if student.gender == 'male':
                    studcompMale['Abjuration'] = studcompMale['Abjuration'] + 1
                else:
                    studcompFemale['Abjuration'] = studcompFemale['Abjuration'] + 1
            elif course.name == 'Conjuration':
                if student.gender == 'male':
                    studcompMale['Conjuration'] = studcompMale['Conjuration'] + 1
                else:
                    studcompFemale['Conjuration'] = studcompFemale['Conjuration'] + 1
            elif course.name == 'Evocation':
                if student.gender == 'male':
                    studcompMale['Evocation'] = studcompMale['Evocation'] + 1
                else:
                    studcompFemale['Evocation'] = studcompFemale['Evocation'] + 1
            elif course.name == 'Illusion':
                if student.gender == 'male':
                    studcompMale['Illusion'] = studcompMale['Illusion'] + 1
                else:
                    studcompFemale['Illusion'] = studcompFemale['Illusion'] + 1
            elif course.name == 'Necromancy':
                if student.gender == 'male':
                    studcompMale['Necromancy'] = studcompMale['Necromancy'] + 1
                else:
                    studcompFemale['Necromancy'] = studcompFemale['Necromancy'] + 1
            elif course.name == 'Transmutation':
                if student.gender == 'male':
                    studcompMale['Transmutation'] = studcompMale['Transmutation'] + 1
                else:
                    studcompFemale['Transmutation'] = studcompFemale['Transmutation'] + 1
    print(studcompMale)
    print(studcompFemale)
    return studcompFemale, studcompMale


def student_completion_barchart(studcompFemale, studcompMale):
    fig, ax = plt.subplots()
    index = np.arange(6)
    bar_width = 0.35
    opacity = 0.8
    rects1 = plt.bar(index, studcompMale.values(), bar_width,
                     alpha=opacity, color='green', label='Males', zorder=3)
    rects2 = plt.bar(index + bar_width, studcompFemale.values(),
                     bar_width, alpha=opacity, color='purple', label='Females', zorder=3)
    plt.xlabel('Courses')
    plt.ylabel('Students')
    plt.title('Students per Course')
    plt.xticks(index + bar_width, (studcompFemale.keys()))
    plt.grid(axis='y', linestyle='dotted', zorder=0)
    plt.legend()
    plt.tick_params()
    plt.show()


if __name__ == "__main__":
    # student_completion_piechart(ex1.ects_completion_categories(ex1.read_students_to_list(csv_students)))
    # students_per_course(ex1.ects_completion_categories(ex1.read_students_to_list(csv_students)))
    student_completion_barchart(students_per_course(
        ex1.read_students_to_list(csv_students))[0], students_per_course(
        ex1.read_students_to_list(csv_students))[1])
