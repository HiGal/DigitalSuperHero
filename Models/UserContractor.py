import hashlib
import SecretConstants
import psycopg2


def db_connect():
    db_name = SecretConstants.DATABASE_NAME
    user = SecretConstants.DATABASE_USER
    password = SecretConstants.DATABASE_PASSWORD
    host = SecretConstants.DATABASE_HOST

    return psycopg2.connect(dbname=db_name, user=user, password=password, host=host)


class UserContractor:
    def __init__(self, email=None, password=None):
        self.conn = db_connect()
        self.email = email
        self.password = password

    def verify(self):
        cursor = self.conn.cursor()
        cursor.execute('select * from user_contractor where email = \'{}\' and password = \'{}\';'
                       .format(self.email, self.password))
        if len(cursor.fetchall()) != 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def register(self, email, password, phone, inn, company_name, reg_date):
        self.email = email
        self.password = hashlib.md5(password.encode()).hexdigest()
        cursor = self.conn.cursor()
        cursor.execute(
            'insert into user_contractor (email, password, phone, inn, company_name, reg_date) '
            'values (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');'.format(
                self.email, self.password, phone, inn, company_name, reg_date)
        )
        self.conn.commit()
        cursor.close()
