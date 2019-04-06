import hashlib
import psycopg2


def db_connect():
    import SecretConstants
    db_name = SecretConstants.DATABASE_NAME
    user = SecretConstants.DATABASE_USER
    password = SecretConstants.DATABASE_PASSWORD
    host = SecretConstants.DATABASE_HOST

    return psycopg2.connect(dbname=db_name, user=user, password=password, host=host)


class UserCustomer:
    phone = str
    name = str
    surname = str
    midname = str

    def __init__(self, email=None, password=None):
        self.conn = db_connect()
        self.email = email
        self.password = password if password is None else hashlib.md5(password.encode()).hexdigest()

    def verify(self) -> bool:
        cursor = self.conn.cursor()
        cursor.execute('select * from user_customer where email = \'{}\' and password = \'{}\';'
                       .format(self.email, self.password))
        if cursor.rowcount == 0:
            cursor.close()
            return False
        else:
            cursor.close()
            return True

    def register(self, email: str, password: str, phone: str, name: str, surname: str, midname: str):
        self.email = email
        self.password = hashlib.md5(password.encode()).hexdigest()
        self.phone = phone
        self.name = name
        self.surname = surname
        self.midname = midname
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO user_customer (email, password, phone, name, surname, midname) '
            'VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(
                self.email, self.password, self.phone, self.name, self.surname, self.midname)
        )
        self.conn.commit()
        cursor.close()

    def retrieve(self) -> bool:
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

        self.phone = record[2]
        self.name = record[3]
        self.surname = record[4]
        self.midname = record[5]

        return True



