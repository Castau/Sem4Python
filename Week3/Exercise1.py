import random
import csv
import os
import matplotlib.pyplot as plt
import numpy as np

# 1) Create 3 classes: Student, DataSheet and Course
# 2) A student has a data_sheet and a data_sheet has multiple courses in particular order
# 3) Each course has name, classroom, teacher, ETCS and optional grade if course is taken.
# 4) In Student create init() so that a Student can be initiated with name, gender,
# data_sheet and image_url
# 5) In DataSheet create a method to get_grades_as_list()
# 6) In student create a method: get_avg_grade()
# 7) Create a function that can generate n number of students with random: name, gender,
# courses(from a fixed list of course names), grades, img_url
# A) Let the function write the result to a csv file with format stud_name, course_name,
# teacher, ects, classroom, grade, img_url
# 8) Read student data into a list of Students from a csv file:
# A) loop through the list and print each student with name, img_url and avg_grade.
# B) sort the list by avg_grade
# C) create a bar chart with student_name on x and avg_grade on y-axis
# 9) Make a method on Student class that can show progression of the study in % (add up
# ECTS from all passed courses divided by total of 150 total points(equivalent to 5 semesters))
# 10) Show a bar chart of distribution of study progression on x-axis and number of students
# in each category on y-axis. (e.g. make 10 categories from 0-100 %)
# Extra: Make the Datasheet class iterable so that next(data_sheet) will return the next
# course in the list


class Student():
    def __init__(self, name, gender, datasheet, imageurl):
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
        self.imageurl = imageurl

    def get_avg_grade(self):
        grades = self.datasheet.get_grades_as_list()
        sumgrades = 0
        for grade in grades:
            sumgrades += int(grade)
        avg = sumgrades/len(grades)
        return avg

    def completed_courses(self):
        completed = int(self.datasheet.get_passed_ECTS())
        return ((completed/150)*100)

    def __repr__(self):
        return 'Student(%r, %r, %r, %r)' % (self.name, self.gender, self.datasheet, self.imageurl)

    def get_courses(self):
        return self.datasheet.get_courses()


class DataSheet():
    def __init__(self, courses=[]):
        self.courses = courses

    def add_course(self, course):
        self.courses.append(course)

    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            grades.append(course.grade)
        return grades

    def __repr__(self):
        return 'DataSheet(%r)' % (self.courses)

    def get_passed_ECTS(self):
        ects = 0
        for course in self.courses:
            if int(course.grade) >= 2:
                ects += int(course.ECTS)
        return ects

    def get_courses(self):
        return self.courses


class Course():
    def __init__(self, name, classroom, teacher, ECTS, grade: int = None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade

    def __repr__(self):
        return 'Course(%r, %r, %r, %r, %r)' % (self.name, self.classroom, self.teacher, self.ECTS, self.grade)


grades = [-3, 0, 2, 4, 7, 10, 12]
classrooms = [101, 103, 105, 107, 109]
ECTS = [5, 10, 20, 30]
courses = ['Abjuration', 'Conjuration',
           'Evocation', 'Illusion', 'Necromancy', 'Transmutation']
genders = ['male', 'female']
males = ['Ultraxion', 'Sartharion', 'Neltharion', 'Kalecgos',
         'Nozdormu', 'Azuregos', 'Nefarian', 'Murozond']
females = ['Ysondre', 'Onyxia', 'Ysera',
           'Alexstrasza', 'Tarecgosa', 'Sindragosa', 'Sinestra', 'Emeriss']
imgurls = ['https://gamepedia.cursecdn.com/wowpedia/4/41/Sindragosa_HS.jpg',
           'https://gamepedia.cursecdn.com/wowpedia/4/40/Onyxia_%28Blackwing_Descent%29.jpg?version=e30e4fac29c7876399ce6a75c830371a',
           'https://gamepedia.cursecdn.com/wowpedia/a/a7/Ultraxion_TCG.jpg?version=08160637051569ef8c6d1668f1f3db85',
           'https://gamepedia.cursecdn.com/wowpedia/1/17/Sartharion.jpg?version=74399c190fa0ccb68834514eaef2fc26',
           'https://gamepedia.cursecdn.com/wowpedia/1/10/Murozond2_TCG.jpg?version=baf06caca832dc59897ceaf313ed90ef',
           'https://gamepedia.cursecdn.com/wowpedia/c/c8/Sinestra_TCG.jpg?version=05d007e67914edaf94ce3023f6f90690',
           'https://gamepedia.cursecdn.com/wowpedia/2/27/Glowei_Deathwing.jpg?version=ce5b668c30b60706f1f4dab21d00a23c',
           'https://gamepedia.cursecdn.com/wowpedia/9/9c/Emerissportal.jpg?version=aebf7d630be651e9bf9fb9ebda0b8759',
           'https://gamepedia.cursecdn.com/wowpedia/2/26/Chronicle3_Hour_of_Twilight.jpg?version=ad583a0516bd3edec21f2de72340e078',
           'https://gamepedia.cursecdn.com/wowpedia/3/34/Dragonqueen_Alexstrasza.jpg?version=9619e081bf4a8649083db0b139dad60e',
           'https://gamepedia.cursecdn.com/wowpedia/2/24/Tarecgosa.jpg']


def createStudents(numofstudents):
    result = []
    result.append(['stud_name', 'course_name',
                   'teacher', 'ects', 'classroom', 'grade', 'img_url'])
    for student in range(0, numofstudents):
        redoStudent = False
        course = random.choice(courses)
        nameCourse = []
        gender = random.choice(genders)

        if gender == 'female':
            name = random.choice(females)
        else:
            name = random.choice(males)

        for row in result:
            if row[0] == name:
                nameCourse.append({row[0]: row[1]})
        dublicate = True

        while dublicate:
            if len(nameCourse) == 0:
                dublicate = False
            if len(nameCourse) == len(courses):
                dublicate = False
                redoStudent = True
                break
            for student in nameCourse:
                if student[name] != course:
                    dublicate = False
                else:
                    copycourses = courses.copy()
                    copycourses.remove(course)
                    course = random.choice(copycourses)
                    dublicate = True
                    break

        if redoStudent == True:
            numofstudents -= 1
            continue

        if course == ('Evocation' or 'Conjuration'):
            teacher = 'Khadgar'
        elif course == ('Abjuration' or 'Illusion'):
            teacher = 'Velen'
        else:
            teacher = 'Medivh'

        img = random.choice(imgurls)
        ects = random.choice(ECTS)
        classroom = random.choice(classrooms)
        grade = random.choice(grades)

        result.append([name, course, teacher, ects, classroom, grade, img])
    return result


def write_students_to_file(outputpath, students: []):
    with open(outputpath+'students.csv', 'w', newline='') as csv_output:
        csvwriter = csv.writer(csv_output)
        for student in students:
            csvwriter.writerow(student)


def read_students_to_list(csvfile):
    students = []
    with open(csvfile) as inputfile:
        csvreader = csv.reader(inputfile)
        header = next(csvreader)
        for row in csvreader:
            if row[0] in females:
                sex = 'female'
            else:
                sex = 'male'
            taken_course = Course(row[1], row[4], row[2], row[3], row[5])
            student_exists = False
            for stud in students:
                if stud.name == row[0]:
                    stud.datasheet.add_course(taken_course)
                    student_exists = True
            if not student_exists:
                data = DataSheet([])
                data.add_course(taken_course)
                student = Student(row[0], sex, data, row[6])
                students.append(student)

        for student in students:
            print(student.name)
            print(student.get_avg_grade())
            print(student.imageurl)
    print()
    return students


def sort_students_by_grade(students, desc: bool = False):
    students_sorted = sorted(
        students, key=lambda student: student.get_avg_grade(), reverse=desc)
    for student in students_sorted:
        print(student.name)
        print(student.get_avg_grade())
    return students_sorted


def avg_grade_student_barchart(students):
    studgrade = {}
    for student in students:
        studgrade[student.name] = student.get_avg_grade()
    plt.figure(figsize=(17, 7))
    plt.bar(studgrade.keys(), studgrade.values(),
            width=0.9, align='center', zorder=3)
    plt.ylim(-3, 12)
    title = 'Average Grade per Student'
    plt.title(title, fontsize=12)
    plt.xlabel("Student Names", fontsize=10)
    plt.ylabel("Average Grades", fontsize=10)
    y = grades.copy()
    plt.yticks(np.arange(min(y), max(y)+1, 1.0))
    plt.grid(axis='y', linestyle='dotted', zorder=0)
    plt.show()


def ects_completion_categories(students):
    studcomp = {}
    studcomp['0-10'] = 0
    studcomp['10-20'] = 0
    studcomp['20-30'] = 0
    studcomp['30-40'] = 0
    studcomp['40-50'] = 0
    studcomp['50-60'] = 0
    studcomp['60-70'] = 0
    studcomp['70-80'] = 0
    studcomp['80-90'] = 0
    studcomp['90-100'] = 0

    for student in students:
        print(student.completed_courses())
        if student.completed_courses() < 10:
            studcomp['0-10'] = studcomp['0-10'] + 1
        elif student.completed_courses() >= 10 and student.completed_courses() < 20:
            studcomp['10-20'] = studcomp['10-20'] + 1
        elif student.completed_courses() >= 20 and student.completed_courses() < 30:
            studcomp['20-30'] = studcomp['20-30'] + 1
        elif student.completed_courses() >= 30 and student.completed_courses() < 40:
            studcomp['30-40'] = studcomp['30-40'] + 1
        elif student.completed_courses() >= 40 and student.completed_courses() < 50:
            studcomp['40-50'] = studcomp['40-50'] + 1
        elif student.completed_courses() >= 50 and student.completed_courses() < 60:
            studcomp['50-60'] = studcomp['50-60'] + 1
        elif student.completed_courses() >= 60 and student.completed_courses() < 70:
            studcomp['60-70'] = studcomp['60-70'] + 1
        elif student.completed_courses() >= 70 and student.completed_courses() < 80:
            studcomp['70-80'] = studcomp['70-80'] + 1
        elif student.completed_courses() >= 80 and student.completed_courses() < 90:
            studcomp['80-90'] = studcomp['80-90'] + 1
        elif student.completed_courses() >= 90 and student.completed_courses() <= 100:
            studcomp['90-100'] = studcomp['90-100'] + 1
    return studcomp


def student_completion_barchart(studcomp):
    plt.figure()
    plt.bar(studcomp.keys(), studcomp.values(),
            width=0.9, align='center', zorder=3)
    title = 'Course Completion in percent'
    plt.title(title, fontsize=12)
    plt.xlabel("Category", fontsize=10)
    plt.ylabel("Students", fontsize=10)
    plt.grid(axis='y', linestyle='dotted', zorder=0)
    plt.show()


week3_path = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week3\\'
csv_students = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week3\\students.csv'

# if __name__ == "__main__":
# write_students_to_file(week3_path, createStudents(50))
# read_students_to_list(csv_students)
#sort_students_by_grade(read_students_to_list(csv_students), True)
# avg_grade_student_barchart(sort_students_by_grade(read_students_to_list(csv_students), True))
# avg_grade_student_barchart(read_students_to_list(csv_students))
# student_completion_barchart(ects_completion_categories(read_students_to_list(csv_students)))
