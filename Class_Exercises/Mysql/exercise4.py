import pymysql
from datetime import datetime, date, timedelta


def create_in_db(table_name, data_dict):
    cnx = pymysql.connect(user='root', password='paragraf119',
                          host='127.0.0.1', port=3306, db='test')
    cursor = cnx.cursor()
    query = (
        "INSERT INTO `test`.`{}` (`firstname`, `lastname`, `startdate`, `enddate`, `salary`) "
        "VALUES (%(firstname)s, %(lastname)s, %(startdate)s, %(enddate)s, %(salary)s);"
    ).format(table_name)
    cursor.execute(query, data_dict)
    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()


hire_start = date(2020, 1, 1)
hire_end = date(2024, 12, 31)
data = {
    'firstname': 'Rigmor',
    'lastname': 'Dragonslayer',
    'startdate': hire_start,
    'enddate': hire_end,
    'salary': 50000
}

create_in_db("pythondemo", data)
print("Check DB...")
