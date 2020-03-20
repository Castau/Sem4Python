from __future__ import print_function

from decimal import Decimal
from datetime import datetime, date, timedelta
import pymysql

# with the build in dict cursor
cnx = pymysql.connect(user='root', password='paragraf119',
                      host='127.0.0.1', port=3306, db='test')

cursor = cnx.cursor(pymysql.cursors.DictCursor)

query = ("SELECT firstname, lastname, startdate, enddate, salary FROM pythondemo")

cursor.execute(query)
print(cursor.fetchall())
