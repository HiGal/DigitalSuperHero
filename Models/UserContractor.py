import hashlib
import SecretConstants

import psycopg2


def db_connect():
    db_name = SecretConstants.DATABASE_NAME
    user = SecretConstants.DATABASE_USER
    password = SecretConstants.DATABASE_PASSWORD
    host = SecretConstants.DATABASE_HOST

    return psycopg2.connect(dbname=db_name, user=user, password=password, host=host)

# email       | password | phone    | INN        |  company_name | reg_date
# varchar(128)| char(32) | char(11) | varchar(12)|  varchar(256) | date


class UserContractor:
    def __init__(self, email=None, password=None):
        self.conn = db_connect()
        self.email = email
        self.password = password

    def verify(self):
        cursor = self.conn.cursor()
        password = self.password
        password = hashlib.md5(password.encode()).hexdigest()
        cursor.execute('select * from user_contractor where email = \'{}\' and password = \'{}\';'
                       .format(self.email, password))
        tmp = cursor.fetchall()
        if len(tmp) != 0:
            cursor.close()
            return True
        cursor.close()
        return False

    def register(self, email, password, phone, inn, company_name, reg_date):
        self.email = email
        self.password = hashlib.md5(password.encode()).hexdigest()
        cursor = self.conn.cursor()
        cursor.execute(
            'insert into user_contractor (email, password, phone, inn, company_name, reg_date) '
            'values (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');'.format(
                email, password, phone, inn, company_name, reg_date)
        )
        self.conn.commit()
        cursor.close()
