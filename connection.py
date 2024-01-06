import pyodbc

# define the server and the database
class connection:
    def __init__(self):
        self.SERVER = 'media-system.database.windows.net' 
        self.DATABASE = 'media-system-db-design'
        self.USERNAME = 'bmkarale'
        self.PASSWORD = 'B.Azure.17'

        # Define the connection string
        connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={self.SERVER};DATABASE={self.DATABASE};UID={self.USERNAME};PWD={self.PASSWORD};Protocol=TCP'
        self.cnxn = pyodbc.connect(connectionString)

        # Create the Cursor.
        self.cursor = self.cnxn.cursor()
        
    def execute_query(self, query, params=None):
        print("Inside Execute query")
        self.cursor.execute(query, params or ())
        self.cnxn.commit()

    def fetch_all(self, query, params=None):
        print("Inside fetch")
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()
        # self.cnxn.commit()
        
    def close(self):
        self.cursor.close()
        self.cnxn.close()
            