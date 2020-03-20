import datetime
import pymysql

cnx = pymysql.connect(user='root', password='paragraf119',
                      host='127.0.0.1', port=3306, db='test')

cursor = cnx.cursor()

query = ("SELECT firstname, lastname, startdate, enddate, salary FROM pythondemo WHERE startdate BETWEEN %s AND %s")

hire_start = datetime.date(1960, 1, 1)
hire_end = datetime.date(2004, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (firstname, lastname, startdate, enddate, salary) in cursor:
    print("{} {} hired from {} to {} is paid: {} DKR pr month".format(
        firstname, lastname, startdate, enddate, salary))

cursor.close()
cnx.close()
