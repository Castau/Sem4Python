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

url_skilte_område = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&CIVILSTAND=U'
csv_skilte_område = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week5\\Downloaded_Files\\skilte_område.csv'

url_område_total = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=TOT&OMR%C3%85DE=*'
csv_område_total = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week5\\Downloaded_Files\\område_total.csv'


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


def line_plot_divorced_people_2008_2020(data_series):
    data_series.plot(zorder=3, marker="*")
    plt.xlabel('Year')
    plt.ylabel('Difference in %')
    plt.title('Yearly difference of divorced people 2008-2020 in %')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='dotted', zorder=0)
    plt.show()


if __name__ == "__main__":
    # webget_mod.download(url_skilte, 'skilte.csv')
    # webget_mod.download(url_skilte_område, 'skilte_område.csv')
    # webget_mod.download(url_område_total, 'område_total.csv')
    line_plot_divorced_people_2008_2020(
        divorced_people_2008_2020_serie(csv_skilte))
