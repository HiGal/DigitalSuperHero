import hashlib

import psycopg2


def db_connect():
    import SecretConstants
    db_name = SecretConstants.DATABASE_NAME
    user = SecretConstants.DATABASE_USER
    password = SecretConstants.DATABASE_PASSWORD
    host = SecretConstants.DATABASE_HOST

    return psycopg2.connect(dbname=db_name, user=user, password=password, host=host)


class UserContractor:

    def __init__(self, email=None, password=None):
        self.conn = db_connect()
        self.email = email
        self.password = password if password is None else hashlib.md5(password.encode()).hexdigest()

    def verify(self) -> bool:
        cursor = self.conn.cursor()
        cursor.execute('select * from user_contractor where email = \'{}\' and password = \'{}\';'
                       .format(self.email, self.password))
        if cursor.rowcount == 0:
            cursor.close()
            return False
        else:
            cursor.close()
            return True

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

    def retrieve(self):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT * FROM user_customer '
            'WHERE email = \'{}\''.format(self.email)
        )

        if cursor.rowcount == 0:
            cursor.close()
            return False

        record = next(cursor)
        cursor.close()
        data = {
            'role': 'contractor',
            'email': record[0],
            'phone': record[2],
            'inn': record[3],
            'company_name': record[4],
            'reg_date': record[5]
        }
        return data
