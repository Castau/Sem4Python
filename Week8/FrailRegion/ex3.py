from flask import Flask
import pandas as pd
from sqlalchemy import create_engine

# Exercise 3
# Lav en restfull webservice (flask) som kan vise dataen fra befkbhalderstatkode.csv
# Takes forever

app = Flask(__name__)


@app.route('/', methods=['GET'])
def showStatskode():
    connectionString = 'mysql+pymysql://user:password@localhost:3306/db'
    engine = create_engine(connectionString)
    df = pd.read_sql_table('statskode', con=engine)
    return df.to_html()


if __name__ == '__main__':
    app.run(debug=True)
