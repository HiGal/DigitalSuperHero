def hash_password(password: str) -> str:
    from hashlib import md5
    return md5(password.encode()).hexdigest()


def db_connect():
    import SecretConstants
    import psycopg2
    dbname = SecretConstants.DATABASE_NAME
    user = SecretConstants.DATABASE_USER
    password = SecretConstants.DATABASE_PASSWORD
    host = SecretConstants.DATABASE_HOST

    return psycopg2.connect(dbname=dbname, user=user, password=password, host=host)


class UserCustomer:
    def __init__(self, email: str = None, password: str = None, phone: str = None, name: str = None,
                 surname: str = None, midname: str = None):
        self.conn = db_connect()
        self.email: str = email
        self.password: str = password
        self.phone: str = phone
        self.name: str = name
        self.surname: str = surname
        self.midname: str = midname
        self.verified = False

    def verify(self) -> bool:
        if self.verified:
            return True

        cursor = self.conn.cursor()
        password = hash_password(self.password)
        cursor.execute(
            'SELECT * FROM user_customer WHERE email = \'{}\' AND password = \'{}\''
                .format(self.email, password)
        )

        count = cursor.rowcount
        cursor.close()

        if count == 0:
            self.verified = False
            return False

        self.verified = True
        return True

    def register(self, email, password, phone, name, surname, midname):
        self.email: str = email
        self.password: str = password
        self.phone: str = phone
        self.name: str = name
        self.surname: str = surname
        self.midname: str = midname

        h_pass = hash_password(password)

        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO user_customer (email, password, phone, name, surname, midname) '
            'VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'
                .format(email, h_pass, phone, name, surname, midname)
        )
        self.conn.commit()
        cursor.close()

        self.verified = True

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
