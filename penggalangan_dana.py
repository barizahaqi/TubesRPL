"""
    Module PenggalanganDana
"""

from . database import Database


class PenggalanganDana:
    """
        Class PenggalanganDana
    """

    def __init__(self, id_penggalangan=None, id_pembuat=None, nama=None, deskripsi=None, dana_dibutuhkan=None, dana_terkumpulkan=None):
        self.__id_penggalangan = id_penggalangan
        self.__id_pembuat = id_pembuat
        self.__nama = nama
        self.__deskripsi = deskripsi
        self.__dana_dibutuhkan = dana_dibutuhkan
        self.__dana_terkumpulkan = dana_terkumpulkan
        self.__db = Database()

    def get_penggalangan_id(self):
        """
            Function get_penggalangan_id
        """
        return self.__id_penggalangan

    def get_pembuat_id(self):
        return self.__id_pembuat

    def get_nama(self):
        """
            Function get_nama
        """
        return self.__nama

    def set_nama(self, nama):
        """
            Function set_nama
        """
        self.__nama = nama
        query = f"UPDATE PenggalanganDana SET Nama = '{self.__nama}' WHERE IDPenggalangan = {self.__id_penggalangan}"
        self.__db.conn.execute(query)
        self.__db.db_connection.commit()

    def get_deskripsi(self):
        """
            Function get_deskripsi
        """
        return self.__deskripsi

    def set_deskripsi(self):
        """
            Function set_deskripsi
        """
        query = f"UPDATE PenggalanganDana SET Deskripsi = '{self.__deskripsi}' WHERE IDPenggalangan = {self.__id_penggalangan}"
        self.__db.conn.execute(query)
        self.__db.db_connection.commit()

    def get_dana_dibutuhkan(self):
        """
            Function get_dana_dibutuhkan
        """
        return self.__dana_dibutuhkan

    def set_dana_dibutuhkan(self, dana):
        self.__dana_dibutuhkan = dana
        query = f"UPDATE PenggalanganDana SET DanaDibutuhkan = {self.__dana_dibutuhkan} WHERE IDPenggalangan = {self.__id_penggalangan}"
        self.__db.conn.execute(query)
        self.__db.db_connection.commit()

    def get_dana_terkumpulkan(self):
        """
            Function get_dana_terkumpulkan
        """
        return self.__dana_terkumpulkan

    def set_dana_terkumpulkan(self, dana):
        """
            Function set_dana
        """
        self.__dana_terkumpulkan = dana
        query = f"UPDATE PenggalanganDana SET DanaTerkumpulkan = {self.__dana_terkumpulkan} WHERE IDPenggalangan = {self.__id_penggalangan}"
        self.__db.conn.execute(query)
        self.__db.db_connection.commit()

    def sisa_dana_belum_terkumpul(self):
        return self.__dana_dibutuhkan - self.__dana_terkumpulkan

    def get_persentase_terkumpul(self):
        """
            Function get_persentase_terkumpul
        """
        return self.__dana_terkumpulkan/self.__dana_dibutuhkan*100
