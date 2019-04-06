import hashlib
import psycopg2


def db_connect():
    import SecretConstants
    db_name = SecretConstants.DATABASE_NAME
    user = SecretConstants.DATABASE_USER
    password = SecretConstants.DATABASE_PASSWORD
    host = SecretConstants.DATABASE_HOST

    return psycopg2.connect(dbname=db_name, user=user, password=password, host=host)


class UserCompany:
    company_name = str
    inn = str
    phone = str

    def __init__(self, email=None, password=None):
        self.conn = db_connect()
        self.email = email
        self.password = password if password is None else hashlib.md5(password.encode()).hexdigest()

    def verify(self) -> bool:
        cursor = self.conn.cursor()
        cursor.execute('select * from user_company where email = \'{}\' and password = \'{}\';'
                       .format(self.email, self.password))
        if cursor.rowcount == 0:
            cursor.close()
            return False
        else:
            cursor.close()
            return True

    def register(self, email: str, password: str, phone: str, company_name: str, inn: str):
        self.email = email
        self.password = hashlib.md5(password.encode()).hexdigest()
        self.phone = phone
        self.company_name = company_name
        self.inn = inn
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO user_company (email, password, phone, company_name, inn) '
            'VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(
                self.email, self.password, self.phone, self.company_name, self.inn)
        )
        self.conn.commit()
        cursor.close()

    def retrieve(self) -> bool:
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT * FROM user_company '
            'WHERE email = \'{}\''.format(self.email)
        )

        if cursor.rowcount == 0:
            cursor.close()
            return False

        record = next(cursor)
        cursor.close()

        self.company_name = record[2]
        self.inn = record[3]
        self.phone = record[4]

        return True
