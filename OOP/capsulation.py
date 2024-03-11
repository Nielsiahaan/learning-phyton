class MyClass:
    def __init__(self):
        self._private_var = 42  # Variable non public dengan awalan satu garis bawah
        self._secret_list = [1, 2, 3]  # Variable non public else

    def _private_method(self):
        print("Ini adalah method non public")

    def public_method(self):
        print("Ini adalah method public")
        self._private_method() # Method public dapat memanggil method non public
