import random
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import webget
from collections import OrderedDict

# Exercise 1
# 1) Open the file './befkbhalderstatkode.csv'
# 2) Turn the csv file into a numpy ndarray with np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
# 3) Using this data:
# neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave',
#           5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst',
#           10: 'Amager Vest', 99: 'Udenfor'}
# Find out how many people lived in each of the 11 areas in 2015
# 4) Make a bar plot to show the size of each city area from the smallest to the largest
# 5) Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015
# 6) How many of those were from the other nordic countries(not dk)
# 7) Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015


week4_path = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week4\\'
csvdata = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week4\\Downloaded_Files\\befkbhalderstatkode.csv'
url = 'https://admin.opendata.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'

districts = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave',
             5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst',
             10: 'Amager Vest', 99: 'Udenfor'}

citizendata = np.genfromtxt(
    csvdata, delimiter=',', dtype=np.uint, skip_header=1)

mask = (citizendata[:, 0] == 2015)


def people_per_district(n, mask):
    all_people_in_district = citizendata[mask & (citizendata[:, 1] == n)]
    sum_of_people = all_people_in_district[:, 4].sum()
    return sum_of_people


citizens_per_area_2015 = np.array(
    [people_per_district(n, mask) for n in districts.keys()])

zipbObj = zip(districts.values(), citizens_per_area_2015)
citizens_per_area_2015_dict = dict(zipbObj)


def sort_districts_per_amount(districts):
    citizens_sorted = OrderedDict(
        sorted(districts.items(), key=lambda x: x[1]))
    return citizens_sorted


def citizens_per_area_barchart(citizens_area):
    plt.figure()
    plt.bar(citizens_area.keys(), citizens_area.values(),
            width=0.7, align='center', zorder=3)
    title = 'Citizens per District 2015'
    plt.title(title, fontsize=15)
    plt.xlabel("Districts", fontsize=12)
    plt.ylabel("No. of citizens", fontsize=12)
    plt.grid(axis='y', linestyle='dotted', zorder=0)
    plt.xticks(rotation=45, ha="right")
    plt.show()


statcodes_nordic = [5110, 5120, 5104, 5105, 5106, 5101, 5901, 5902]


def citizens_over_65_2015(citizendata):
    filtereddata = citizendata[(citizendata[:, 0] == 2015)
                               & (citizendata[:, 2] > 65) & (np.in1d(citizendata[:, 3], statcodes_nordic))]
    sum_of_people = filtereddata[:, 4].sum()
    print(citizendata[:, 3])
    print(filtereddata)
    return sum_of_people


def citizens_vesterbro_østerbro(citizendata):
    v_ø_districts = [2, 4]
    years = [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002,
             2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

    østerbro = np.array(
        [np.sum(citizendata[((citizendata[:, 1] == 2) & (citizendata[:, 0] == year))][:, 4]) for year in years])

    vesterbro = np.array(
        [np.sum(citizendata[((citizendata[:, 1] == 4) & (citizendata[:, 0] == year))][:, 4]) for year in years])

    filtereddata = citizendata[(np.in1d(citizendata[:, 1], v_ø_districts))]
    print(østerbro)
    print(vesterbro)
    return østerbro, vesterbro, years


def line_plot_østerbro_vesterbro(øst, vest, years):
    fig, ax = plt.subplots()
    index = np.arange(len(years))
    rects1 = plt.plot(øst, linewidth=3, color='green',
                      label='Østerbro', zorder=3)
    rects2 = plt.plot(vest, linewidth=3, color='blue',
                      label='Vesterbro', zorder=3)
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population in Østerbro and Vesterbro 1992-2015')
    plt.xticks(index, (years), rotation=45)
    plt.grid(axis='y', linestyle='dotted', zorder=0)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # webget.download(url)
    # citizens_per_area_barchart(
    #     sort_districts_per_amount(citizens_per_area_2015_dict))
    # print(citizens_over_65_2015(citizendata))
    # citizens_vesterbro_østerbro(citizendata)
    line_plot_østerbro_vesterbro(citizens_vesterbro_østerbro(citizendata)[
                                 0], citizens_vesterbro_østerbro(citizendata)[1], citizens_vesterbro_østerbro(citizendata)[2])
