from connection import connection

class SongDAO:
    def __init__(self):
        print("here")

    def get_connection(self):
        print("Got connection")
        db = connection()
        return db
        

    def get_all_songs(self):
        db = self.get_connection()
        select_query = "select * from Song;"
        rows = db.fetch_all(select_query)
        for row in rows:
            print(row)

    def insert_song_media(self, songMediaID):
        db = self.get_connection()
        insert_in_med_query = 'insert into Media (MediaID) values (?)'
        db.execute_query(insert_in_med_query, songMediaID)
        select_media_query = "select * from Media;"
        rows1 = db.fetch_all(select_media_query)
        for row in rows1:
            print(row)

    def insert_song(self, songMediaID, duration, songTitle, songRoyaltyRate,songCountry,songLanguage, songAlbumID, songTrackNumber, songreleaseDate):
        db = self.get_connection()
        # Modify the query to include placeholders
        insert_in_song_query = "insert into Song (MediaID, ReleaseDate, Duration, Title, RoyaltyRate, Country, Language, AlbumID, TrackNumber) values (?, ?, ?, ?, ?, ?, ?, ?, ?)"

        # Create a parameter tuple containing all the values
        params = (songMediaID, songreleaseDate, duration, songTitle, songRoyaltyRate, songCountry, songLanguage, songAlbumID, songTrackNumber)

        # Execute the query with the parameter tuple
        db.execute_query(insert_in_song_query, params)

        # for row in row1:
        #     print(row)
        # rows_fetch = db.fetch_all(insert_in_song_query)
        # for row in rows_fetch:
        #     print(row)

    def update_song(self, updatesongmediaid, updatesongtitle):
        db = self.get_connection()
        update_in_song_query = "update song set Title = ? where MediaID = ?"
        db.execute_query(update_in_song_query, ( updatesongmediaid, updatesongtitle))


    def delete_song(self, deletesong):
        db = self.get_connection()

        # Delete from Media table
        delete_from_media_query = "DELETE FROM Media WHERE MediaID = ?"
        db.execute_query(delete_from_media_query, deletesong)
        # Delete from Song table
        delete_from_song_query = "DELETE FROM Song WHERE MediaID = ?"
        db.execute_query(delete_from_song_query, deletesong)


    # insert_query = "insert into Media DEFAULT VALUES;"
    # db.execute_query(insert_query)
    # select_media_query = "select * from Media;"
    # rows1 = db.fetch_all(select_media_query)
    # for row in rows1:
    #     print(rows1)
