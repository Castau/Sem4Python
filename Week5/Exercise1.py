import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import webget_mod

# 1) Go to https: // www.dst.dk/da/Statistik/statistikbanken/api
# 2) Open 'Konsol' and click 'Start Konsol'
# 3) In the console at pt 1: choose 'Retrieve tables' pt 2: choose get request and json format and pt 3: execute:
# A) check the result
# B) in the code below this same get request is used to get information about all available data tables in 'databanken'.
# 4) Change pt. 1 in the console to 'Retrieve data' pt 2: get request and Table id: 'FOLK1A', format: csv, delimiter: semicolon and click: 'Variable and value codes' and choose some sub categories(Hint: hover over the codes to see their meaning). Finally execute and see what data you get.
# 5) With data aggregation and data visualization answer the following questions:
# A) What is the change in pct of divorced danes from 2008 to 2020?
# B) Which of the 5 biggest cities has the highest percentage of 'Never Married'?
# C) Show a bar chart of changes in marrital status in Copenhagen from 2008 till now
# D) Show a bar chart of 'Married' and 'Never Married' for all ages in DK(Hint: 2 bars of different color)


url_skilte = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=F&Tid=2008K1%2C2009K1%2C2010K1%2C2011K1%2C2012K1%2C2013K1%2C2014K1%2C2015K1%2C2016K1%2C2017K1%2C2018K1%2C2019K1%2C2020K1'
csv_skilte = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week5\\Downloaded_Files\\skilte.csv'

url_skilte_område_total = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Tid=2020K1&CIVILSTAND=TOT%2CU&K%C3%98N=TOT&OMR%C3%85DE=101%2C851%2C561%2C461%2C751&ALDER=IALT'
csv_skilte_område_total = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week5\\Downloaded_Files\\skilte_område_total.csv'

url_copenhagen_marrital_status_2008_2020 = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=101&CIVILSTAND=U%2CG%2CE%2CF&Tid=2008K1%2C2009K1%2C2010K1%2C2011K1%2C2012K1%2C2013K1%2C2014K1%2C2015K1%2C2016K1%2C2017K1%2C2018K1%2C2019K1%2C2020K1'
csv_copenhagen_marrital_status_2008_2020 = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week5\\Downloaded_Files\\copenhagen_marrital_status_2008_2020.csv'

url_unmarried_married_all_ages = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&ALDER=*&CIVILSTAND=U%2CG'
csv_unmarried_married_all_ages = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week5\\Downloaded_Files\\unmarried_married_all_ages.csv'

# A)
def divorced_people_2008_2020_serie(file):
    data_skilte = pd.read_csv(file, delimiter=';')
    divorced = np.array(data_skilte.iloc[:, 2])
    divorced_procent = []

    for i, amount in enumerate(divorced):
        if i == 0:
            divorced_procent.append(0)
        else:
            divorced_procent.append(
                ((divorced[i]-divorced[i-1])/divorced[i-1])*100)

    skilte_serie = pd.Series(
        divorced_procent, index=np.array(data_skilte.iloc[:, 1]))
    print(skilte_serie)
    return skilte_serie


def line_plot_divorced_people_2008_2020(data):
    data.plot(zorder=3, marker="*")
    plt.xlabel('Year')
    plt.ylabel('Difference in %')
    plt.title('Yearly difference of divorced people 2008-2020 in %')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='dotted', zorder=0)
    plt.show()

# B)
def never_married_biggest_cities(file):
    # Thomas' solutions from slack
    data = pd.read_csv(file, delimiter=';')
    # Same result, but with dict comprehension
    # not_married_pct = {data['OMRÅDE'][not_married][4:]: data['INDHOLD'][not_married] / data['INDHOLD'][all_people]*100 for not_married, all_people in zip(range(5, 10), range(0, 5))}
    # sorted(not_married_pct, key=not_married_pct.get, reverse=True)
    result = {}
    for not_married, all_people in zip(range(5, 10), range(0, 5)):
        pct_not_married = data['INDHOLD'][not_married] / \
            data['INDHOLD'][all_people]*100
        city = data['OMRÅDE'][not_married][4:]
        result[city] = pct_not_married
    return result


def bar_plot_never_married_biggest_cities(data):
    plt.figure()
    plt.bar(data.keys(), data.values(),
            width=0.4, align='center', zorder=3)
    title = 'Percent never married pr. city'
    plt.title(title, fontsize=15)
    plt.xlabel("Cities", fontsize=12)
    plt.ylabel("Percent never married", fontsize=12)
    plt.grid(axis='y', linestyle='dotted', zorder=0)
    plt.xticks(rotation=45, ha="right")
    plt.show()


# C)
def copenhagen_marrital_status_2008_2020(file):
    data = pd.read_csv(file, delimiter=';')
    gift = data[data['CIVILSTAND'] == 'Gift/separeret']
    ugift = data[data['CIVILSTAND'] == 'Ugift']
    fraskilt = data[data['CIVILSTAND'] == 'Fraskilt']
    enke = data[data['CIVILSTAND'] == 'Enke/enkemand']

    return gift, ugift, fraskilt, enke


def bar_plot_copenhagen_marrital_status_2008_2020(data_gift, data_ugift, data_fraskilt, data_enke):
    plt.figure()
    p1 = plt.bar(data_ugift['TID'], data_ugift['INDHOLD'],
                 width=0.5, align='center', color='teal', zorder=3)
    p2 = plt.bar(data_gift['TID'], data_gift['INDHOLD'],
                 width=0.5, align='center', color='steelblue', zorder=3)
    p3 = plt.bar(data_fraskilt['TID'], data_fraskilt['INDHOLD'],
                 width=0.5, align='center', color='slateblue', zorder=3)
    p4 = plt.bar(data_enke['TID'], data_enke['INDHOLD'],
                 width=0.5, align='center', color='rebeccapurple', zorder=3)
    plt.title('Civilstand København 2008-2020', fontsize=15)
    plt.xlabel("År", fontsize=12)
    plt.ylabel("Civilstand", fontsize=12)
    plt.legend([p1, p2, p3, p4], ['Ugift', 'Gift', 'Fraskilt', 'Enke'], loc=1)
    plt.grid(axis='y', linestyle='dotted', zorder=0)
    plt.xticks(rotation=45, ha="right")
    plt.show()


# D) 
def unmarried_married_all_ages(file):
    rawdata = pd.read_csv(file, delimiter=';')
    data = rawdata[rawdata['ALDER'] != 'I alt']
    gift = data[data['CIVILSTAND'] == 'Gift/separeret']
    ugift = data[data['CIVILSTAND'] == 'Ugift']
    return gift, ugift


def bar_plot_unmarried_married_all_ages(data_gift, data_ugift):
    plt.figure()
    index = np.arange(126)
    bar_width = 0.2
    p1 = plt.bar(index, data_ugift['INDHOLD'],
                 bar_width, color='lightcoral', zorder=3)
    p2 = plt.bar(index + bar_width, data_gift['INDHOLD'],
                 bar_width, color='steelblue', zorder=3)
    plt.title('Gift vs. Ugift alle aldre', fontsize=15)
    plt.xlabel("Alder", fontsize=12)
    plt.ylabel("Antal", fontsize=12)
    plt.legend([p1, p2], ['Ugift', 'Gift'], loc=1)
    plt.grid(axis='y', linestyle='dotted', zorder=0)
    plt.xticks(index + bar_width, data_ugift['ALDER'], rotation=90)
    plt.show()



if __name__ == "__main__":
    # webget_mod.download(url_skilte, 'skilte.csv')
    # webget_mod.download(url_skilte_område_total, 'skilte_område_total.csv')
    # webget_mod.download(url_copenhagen_marrital_status_2008_2020, 'copenhagen_marrital_status_2008_2020.csv')
    # webget_mod.download(url_unmarried_married_all_ages,'unmarried_married_all_ages.csv')
    # line_plot_divorced_people_2008_2020(divorced_people_2008_2020_serie(csv_skilte))
    # bar_plot_never_married_biggest_cities(never_married_biggest_cities(csv_skilte_område_total))
    # bar_plot_copenhagen_marrital_status_2008_2020(
    #     copenhagen_marrital_status_2008_2020(csv_copenhagen_marrital_status_2008_2020)[0], 
    #     copenhagen_marrital_status_2008_2020(csv_copenhagen_marrital_status_2008_2020)[1], 
    #     copenhagen_marrital_status_2008_2020(csv_copenhagen_marrital_status_2008_2020)[2], 
    #     copenhagen_marrital_status_2008_2020(csv_copenhagen_marrital_status_2008_2020)[3])
    bar_plot_unmarried_married_all_ages(unmarried_married_all_ages(csv_unmarried_married_all_ages)[0], 
                                        unmarried_married_all_ages(csv_unmarried_married_all_ages)[1])
