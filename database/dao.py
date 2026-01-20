from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                    FROM artist a """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_connessione():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = ("""SELECT DISTINCT a1.id as artista1, a2.id as artista2, COUNT(t1.genre_id = t2.genre_id) as peso
                    FROM artist a1, artist a2, track t1,track t2, album al1, album al2
                    WHERE a1.id = al1.artist_id AND  a2.id = al2.artist_id AND  al1.id =t1.album_id AND al2.id =t2.album_id
                            AND t1.genre_id = t2.genre_id  and a1.id <> a2.id
                    GROUP by artista1, artista2 """ )
        try:
            cursor.execute(query)
            for row in cursor:
                connessione = (row['artista1'], row['artista2'], row['peso'])


                result.append(connessione)

        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    def get_all_artists_min_albums(self, min_albums):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT a.id, a.name, COUNT(al.id) as num
                    FROM artist a, album al 
                    WHERE a.id = al.artist_id AND num >= min_albums
                    GROUP BY a.id"""
        cursor.execute(query, (min_albums,))
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'], num = row["num"])
            result.append(artist)
        cursor.close()
        conn.close()
        return result




    
    





