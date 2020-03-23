import pandas as pd
import pymysql
from sqlalchemy import create_engine
import re

connectionString = 'mysql+pymysql://user:password@localhost:3306/db'


# Exercise1:
# http://samplecsvs.s3.amazonaws.com/SacramentocrimeJanuary2006.csv
# Download data fra linket og gem det i en dataframe
# og gem det i en mysql database
def ex1():
    url = "http://samplecsvs.s3.amazonaws.com/SacramentocrimeJanuary2006.csv"
    dataframe = pd.read_csv(url)
    engine = create_engine(connectionString)
    dataframe.to_sql('sacramentocrime', con=engine,
                     if_exists='append', index=False)
    print('Succes!')


# Exercise2:
# Lav en funktion der returnerer en dict med minimum følgende data:
# - Find antallet af crimes mellem to givne datoer i 2006 (givet som parameter til funktionen)
# - Find den totale mængde af "burglary" i januar
def ex2(startDay=None, endDay=None):
    engine = create_engine(connectionString)
    dataframe = pd.read_sql_table('sacramentocrime', con=engine, parse_dates=[
        'cdatetime'], columns=['cdatetime', 'crimedescr'])
    if (startDay and endDay):
        if(int(startDay) > int(endDay)):
            return f'Requested start day ({startDay}) is greater than end day ({endDay})'
        if(int(endDay) > 31):
            return f'Last day of Janyary is the 31st - the end day ({endDay}) cannot be greater than 31'
        startDate = '2006-01-' + startDay + " 00:00"
        endDate = '2006-01-' + endDay + " 23:59"
        crimes = dataframe.loc[(dataframe['cdatetime'] >= startDate)
                               & (dataframe['cdatetime'] <= endDate)]
        return {f'Amount of crimes between {startDate} and {endDate}': len(crimes)}

    burglaries = dataframe[dataframe['crimedescr'].str.contains(
        'BURGLARY')]
    return {'Amount of burglaries in January': len(burglaries)}


# if __name__ == '__main__':
    # ex1()
    # print(ex2('07', '13'))
    # print(ex2('11', '09'))
    # print(ex2('17'))
    # print(ex2('11', '55'))
    # print(ex2())
