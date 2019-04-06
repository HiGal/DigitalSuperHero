from enum import Enum


class OrderStage(Enum):
    REQUESTS = 1
    ANALYSIS = 2
    SEARCH = 3
    WAITING = 4
    CHECK = 5
    DONE = 6


def db_connect():
    import SecretConstants
    import psycopg2
    dbname = SecretConstants.DATABASE_NAME
    user = SecretConstants.DATABASE_USER
    password = SecretConstants.DATABASE_PASSWORD
    host = SecretConstants.DATABASE_HOST

    return psycopg2.connect(dbname=dbname, user=user, password=password, host=host)


class Order:

    def __init__(self, stage: OrderStage = None, task: str = None, customer_email: str = None, description: str = None,
                 attachments: bytes = None):
        self.id: int = -1
        self.stage: OrderStage = stage
        self.task: str = task
        self.description: str = description
        self.customer_email: str = customer_email

        if bytes is None:
            self.attachments = b'0'
        else:
            self.attachments: bytes = attachments

        self.conn = db_connect()

    def register(self, stage: OrderStage, task: str, description: str, customer_email: str):
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO orders (stage, task, description, customer_email) '
            'VALUES (%s, %s, %s, %s) RETURNING id',
            (stage.name.lower(), task, description, customer_email)
        )
        self.conn.commit()

        self.id = cursor.fetchone()[0]
        cursor.close()

        self.stage = stage
        self.task = task
        self.description = description
        self.customer_email = customer_email

    def retrieve(self, id: int):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT stage, task, description, customer_email FROM orders WHERE id = %s', [id]
        )

        if cursor.rowcount == 0:
            return False

        record = next(cursor)
        cursor.close()

        self.id = id
        self.stage = record[0]
        self.task = record[1]
        self.description = record[2]
        self.customer_email = record[3]

        return True

    def change_stage(self, new_stage: OrderStage) -> bool:
        if abs(self.stage.value - new_stage.value) > 1:
            return False

        cursor = self.conn.cursor()
        cursor.execute(
            'UPDATE orders SET stage = %s WHERE id = %s', (new_stage.name.lower(), self.id)
        )
        self.conn.commit()
        cursor.close()
        self.stage = new_stage

        return True

    def set_attachment(self, attachment: bytes):
        cursor = self.conn.cursor()
        cursor.execute(
            'UPDATE orders SET attachments = %s WHERE customer_email = %s',
            (attachment, self.customer_email)
        )
        self.conn.commit()
        cursor.close()

    def get_attachment(self) -> bytes:
        if self.attachments is not None:
            return self.attachments

        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT attachments FROM orders WHERE id = %s', [self.id]
        )

        if cursor.rowcount == 0:
            return b'0'

        record = next(cursor)
        cursor.close()

        return record[0]
