import pandas as pd
import pymysql
from sqlalchemy import create_engine

csv = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Class_Exercises\\Mysql\\cars.csv'
con_str = 'mysql+pymysql://root:paragraf119@localhost:3306/test'
engine = create_engine(con_str)

df = pd.read_csv(csv, delimiter=',')

df.to_sql('cars', con=engine, if_exists='append', index=False)
print(df.dtypes)
