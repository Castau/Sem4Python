from flask import Flask, jsonify, abort, request
from sqlalchemy import create_engine
import pandas as pd
import pymysql
from collections import OrderedDict


# Exercise 1
# Brug test.sql scriptet(pythondemo):
# Hent følgende data:
# Navn på de personer som har en salary der er højere end 50.000
# Navn på dem som har efternavnet Juhlborg
def exercise1(query):
    connection = pymysql.connect(user='user', password='password',
                                 host='127.0.0.1', port=3306, db='test')
    result = []
    with connection.cursor() as cursor:
        cursor.execute(query)
        for firstname, lastname in cursor:
            result.append({firstname, lastname})
    connection.close()
    return result


salaryQuery = "SELECT firstname, lastname FROM test.pythondemo WHERE salary > 50000;"
lastnameQuery = "SELECT firstname, lastname FROM test.pythondemo WHERE lastname = 'Juhlborg';"

print('Personer som har en salary der er højere end 50.000:', exercise1(salaryQuery))
print('Personer som har efternavnet Juhlborg:', exercise1(lastnameQuery))


# Exercise 2
# Anvend filen: befkbhalderstatkode.csv
# Lav denne fil om til en mysql table med navnet statskode
def exercise2():
    connectionString = 'mysql+pymysql://user:password@localhost:3306/db'
    url = 'https://admin.opendata.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'
    dataframe = pd.read_csv(url)
    engine = create_engine(connectionString)
    dataframe.to_sql('statskode', con=engine,
                     if_exists='replace', index=False)
    print('Succes!')


exercise2()
