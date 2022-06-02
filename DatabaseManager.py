import psycopg2
from configparser import ConfigParser


class DatabaseConnect:
    def __init__(self, filename="./configs/database.ini", section="postgresql"):
        self.filename = filename
        self.section = section

    def config(self):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(self.filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(self.section):
            params = parser.items(self.section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception(f"Section {0} not found in the {1} file")

        return db

    def connect(self):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            params = self.config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()

            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)

            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

    def insert_into_client(self, name: str, surname: str, address: str):
        query: str = f"""INSERT INTO clients (client_name, surname, address) 
        VALUES (%s, %s, %s) RETURNING client_id;"""

        conn = None
        clientId = None

        try:
            # read the db configuration
            params = self.config()
            # connect to the db
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute query
            cur.execute(query, (name, surname, address))
            # get generated id
            clientId = cur.fetchone()[0]
            # commit changes
            conn.commit()
            # close communication
            cur.close()



        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()
        return clientId

    def insert_into_product(self, product_name: str, price: int, amount: int = 0):
        query: str = f"""INSERT INTO products (product_name, price, amount) 
        VALUES (%s, %s, %s) RETURNING sku;"""

        conn = None
        sku = None

        try:
            # read the db configuration
            params = self.config()
            # connect to the db
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute query
            cur.execute(query, (product_name, price, amount))
            # get generated id
            clientId = cur.fetchone()[0]
            # commit changes
            conn.commit()
            # close communication
            cur.close()


        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()
        return sku

    def select_customer(self, client_id: int):
        query: str = f"""SELECT * FROM clients WHERE client_id = %s"""
        conn = None
        result: None = None
        try:
            # read the db configuration
            params = self.config()
            # connect to the db
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute query
            cur.execute(query, (client_id,))
            # save results
            result: tuple = cur.fetchone()

            # close communication
            cur.close()
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()
        return result


if __name__ == "__main__":
    conf = DatabaseConnect()
