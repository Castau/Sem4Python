# sqlalchemy helped convert strings to dates seamlessly
from sqlalchemy import create_engine
import pandas as pd
import pymysql

cnx = pymysql.connect(user='root', password='paragraf119',
                      host='127.0.0.1', port=3306, db='test')

df = pd.read_sql('SELECT * FROM pythondemo', con=cnx)
print(df)


#cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test')
con_str = 'mysql+pymysql://root:paragraf119@localhost:3306/test'
engine = create_engine(con_str)

df = pd.DataFrame({'firstname': ['Ulrik', 'Ulla', 'Ulfred'],
                   'lastname': ['Volborg', 'Willman', 'Valberg'],
                   'startdate': ['2003-03-03', '2001-05-04', '2001-01-04'],
                   'enddate': ['2005-08-20', '2005-12-24', '2006-10-30'],
                   'salary': ['21000', '32000', '43000']})
#df = df.applymap(str)
df.to_sql('pythondemo', con=engine, if_exists='append', index=False)
print(df.dtypes)
