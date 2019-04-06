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


class UserCompany:
    def __init__(self, email: str = None, password: str = None, phone: str = None, company: str = None,
                 INN: str = None):
        self.conn = db_connect()
        self.email: str = email
        self.password: str = password if password is None else hash_password(password)
        self.phone: str = phone
        self.company: str = company
        self.INN: str = INN
        self.verified: bool = False

    def verify(self) -> bool:
        if self.verified:
            return True

        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT * FROM user_company WHERE email = \'{}\' AND password = \'{}\''
                .format(self.email, self.password)
        )

        count = cursor.rowcount
        cursor.close()

        if count == 0:
            self.verified = False
            return False

        self.verified = True
        return True

    def register(self, email: str, password: str, phone: str, company: str, inn: str):
        self.email: str = email
        self.password: str = password
        self.company: str = company
        self.INN: str = inn

        h_pass = hash_password(password)

        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO user_company (email, password, phone, company_name, inn) '
            'VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'
                .format(email, h_pass, phone, company, inn)
        )
        self.conn.commit()
        cursor.close()

        self.verified = True

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

        self.company = record[2]
        self.INN = record[3]
        self.phone = record[4]

        return True
