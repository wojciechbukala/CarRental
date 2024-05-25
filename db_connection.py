import psycopg2

#local db port: 5432
#port flaska: 5000
#docker master port: 5001
#docker slave port: 5002

class Database:
    def __init__(self, dbname, user, password, host="localhost", port=5432):
        self.conn = psycopg2.connect(
            dbname = dbname,
            user = user,
            password = password,
            host = host,
            port = port
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()