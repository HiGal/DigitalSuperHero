import hashlib
import SecretConstants

import psycopg2


def db_connect():
    dbname = SecretConstants.DATABASE_NAME
    user = SecretConstants.DATABASE_USER
    password = SecretConstants.DATABASE_PASSWORD
    host = SecretConstants.DATABASE_HOST

    return psycopg2.connect(dbname=dbname, user=user, password=password, host=host)


class User:
    def __init__(self, username=None, password=None):
        self.conn = db_connect()
        self.username = username
        self.password = password

    def verify(self):
        cursor = self.conn.cursor()
        password = self.password
        password = hashlib.md5(password.encode()).hexdigest()
        cursor.execute('select * from sys_user where username = \'{}\' and password = \'{}\';'
                       .format(self.username, password))
        tmp = cursor.fetchall()
        if len(tmp) != 0:
            cursor.close()
            return True
        cursor.close()
        return False

    def register(self, username, password, name, sname, email, bdate):
        password = hashlib.md5(password.encode()).hexdigest()
        self.password = password
        self.username = username
        cursor = self.conn.cursor()
        cursor.execute(
            'insert into sys_user (username, password,name, surname, email,birthday) '
            'values (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');'.format(username, password, name, sname, email, bdate)
        )
        self.conn.commit()
        cursor.close()
