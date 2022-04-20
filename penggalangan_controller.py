"""
    Module PenggalanganDanaController
"""

from . database import Database


class PenggalanganController:
    """
        Class PenggalanganDanaController
    """

    def __init__(self):
        database = Database()
        query = f"SELECT * FROM PenggalanganDana"
        database.conn.execute(query)
        self.__list_penggalangan_buff = database.conn.fetchall()
        database.conn.close()

    def make_penggalangan(self, id_pengguna, nama, deskripsi, dana_dibutuhkan):
        """
            Function make_penggalangan
        """
        database = Database()
        query_len_penggalangan = "SELECT COUNT(*) FROM PenggalanganDana"
        database.conn.execute(query_len_penggalangan)
        # self.__db.conn.execute(query_len_penggalangan)
        len_penggalangan = self.__db.conn.fetchone()[0]
        query = f"INSERT INTO PenggalanganDana VALUES ({len_penggalangan+1}, {id_pengguna}, '{nama}', '{deskripsi}', {dana_dibutuhkan}, {0})"
        database.conn.execute(query)
        database.commit()
        # self.__db.conn.execute(query)
        # self.__db.db_connection.commit()

    def get_penggalangan_by_id_penggalangan(self, id_penggalangan):
        """
            Function get_penggalangan
        """
        database = Database()
        query = f"SELECT * FROM PenggalanganDana WHERE IDPenggalangan = {id_penggalangan}"
        database.conn.execute(query)
        # self.__db.conn.execute(query)
        # return self.__db.conn.fetchone()
        return database.conn.fetchone()

    def get_penggalangan_by_id_pengguna(self, id_pengguna):
        database = Database()
        query = f"SELECT * FROM PenggalanganDana"
        database.conn.execute(query)
        self.__list_penggalangan_buff = database.conn.fetchall()
        query = f"SELECT * FROM PenggalanganDana WHERE IDPengguna = {id_pengguna}"
        database.conn.execute(query)
        return database.conn.fetchall()
        # self.__db.conn.execute(query)
        # return self.__db.conn.fetchall()

    def get_all_penggalangan(self):
        database = Database()
        query = f"SELECT * FROM PenggalanganDana"
        database.conn.execute(query)
        self.__list_penggalangan_buff = database.conn.fetchall()
        query = f"SELECT * FROM PenggalanganDana"
        database.conn.execute(query)
        return database.conn.fetchall()
        # self.__db.conn.execute(query)
        # return self.__db.conn.fetchall()

    def delete_penggalangan(self, id_penggalangan):
        """
            Function delete_penggalangan
        """
        database = Database()
        query = f"DELETE FROM PenggalanganDana WHERE IDPenggalangan = {id_penggalangan}"
        # self.__db.conn.execute(query)
        # self.__db.db_connection.commit()
        database.conn.execute(query)
        database.commit()

    def get_banyak_penggalangan(self):
        """
            Function get_banyak_penggalangan
        """
        database = Database()
        query = "SELECT COUNT(*) FROM PenggalanganDana"
        database.conn.execute(query)
        return database.conn.fetchone()[0]
        # self.__db.conn.execute(query)
        # return self.__db.conn.fetchone()[0]

    # Mencari penggalangan berdasarkan nama str2ang mendekati
    def cari_penggalangan(self, nama):
        """
            Function cari_penggalangan
        """
        # database = Database()
        # query = f"SELECT * FROM PenggalanganDana"
        # database.conn.execute(query)
        # self.__db.conn.execute(query)
        # list_penggalangan = self.__db.conn.fetchall()
        list_penggalangan = self.__list_penggalangan_buff
        list_penggalangan_terdekat = []

        for penggalangan in list_penggalangan:
            string_nama = nama.split()
            nama_penggalangan = penggalangan[2]
            deskripsi = penggalangan[3]
            for word in string_nama:
                if word.lower() in nama_penggalangan.lower():
                    list_penggalangan_terdekat.append(penggalangan)
                    break
                if word.lower() in deskripsi.lower():
                    list_penggalangan_terdekat.append(penggalangan)
                    break
        return list_penggalangan_terdekat
