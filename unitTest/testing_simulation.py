import unittest


def connection_db():
    print("[terhubung ke db]")


def putus_koneksi_db(db):
    print("[tidak terhubung ke db {}]".format(db))


class User:
    username = ""
    active = False

    def __init__(self, db, username):  # using db sample
        self.username = username

    def set_active(self):
        self.active = True


class TestUser(unittest.TestCase):
    # # Test Case 1
    # def test_user_default_not_active(self):
    #     db = connection_db()
    #     dicoding = User(db, "dicoding")
    #     self.assertFalse(dicoding.active)  # tidak aktif secara default
    #     putus_koneksi_db(db)
    #
    # # Test case 2
    # def test_user_is_active(self):
    #     db = connection_db()
    #     dicoding = User(db, "dicoding")
    #     dicoding.set_active()  # activate new user
    #     self.assertTrue(dicoding.active)
    #     putus_koneksi_db(db)

    '''
    Metode setUp(), sesuai namanya, bertujuan untuk mempersiapkan pengujian. Metode ini akan dipanggil untuk menyiapkan tes sehingga pemanggilannya akan dilakukan tiap sebelum metode tes dilaksanakan.
    Metode tearDown() akan dipanggil setiap metode tes selesai dilaksanakan dan bertindak untuk membersihkan, meskipun terjadi kesalahan (exception) pada proses tes.
    '''

    # Menggunakan metode setUp() dan tearDown()
    # Test Fixture
    def setUp(self):
        self.db = connection_db()
        self.dicoding = User(self.db, "dicoding")

    def tearDown(self):
        putus_koneksi_db(self.db)

    # Test case 1
    def test_user_default_not_active(self):
        # non active as default
        self.assertFalse(self.dicoding.active)

    # Test case 2
    def test_user_is_active(self):
        # activate new user
        self.dicoding.set_active()
        self.assertTrue(self.dicoding.active)


if __name__ == '__main__':
    # Test runner
    unittest.main()
