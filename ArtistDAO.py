from connection import connection

class ArtistDAO:
    def __init__(self):
        print("In ArtistDAO init")

    def get_connection(self):
        print("Got connection")
        db = connection()
        return db
    
    def get_all_artists(self):
        db = self.get_connection()
        select_query = "select * from Artist;"
        rows = db.fetch_all(select_query)
        for row in rows:
            print(row)

    def delete_artist(self, deleteArtistID):
        db = self.get_connection()
        delete_query = "delete from Artist where ArtistID = ?"
        db.execute_query(delete_query, deleteArtistID)

    def update_artist(self, artistName):
        db = self.get_connection()
        update_query = "update Artist set Name = ?"
        db.execute_query(update_query, artistName)

    def insert_artist(self, ArtistID, Name, Status, Type, Country, PrimaryGenre):
        db = self.get_connection()
        insert_query = "INSERT INTO Artist (ArtistID, Name, Status, Type, Country, PrimaryGenre) VALUES (?, ?, ?, ?, ?, ?)"
        params = (ArtistID, Name, Status, Type, Country, PrimaryGenre)
        db.execute_query(insert_query, params)