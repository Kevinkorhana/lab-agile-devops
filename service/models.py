import logging

class DataValidationError(Exception):
    """Digunakan untuk error validasi data"""
    pass

class Account:
    """Model representasi data Account"""
    logger = logging.getLogger("flask.app")
    data = {}
    index = 0

    def __init__(self, id=None, name=None, email=None):
        self.id = id
        self.name = name
        self.email = email

    def create(self):
        """Membuat Account baru"""
        if not self.name or not self.email:
            raise DataValidationError("Name and Email cannot be empty")
        Account.index += 1
        self.id = Account.index
        Account.data[self.id] = self
        return self

    def update(self):
        """Mengupdate Account yang sudah ada"""
        if not self.id or self.id not in Account.data:
            raise DataValidationError("Account not found")
        Account.data[self.id] = self
        return self

    def delete(self):
        """Menghapus Account"""
        if self.id in Account.data:
            del Account.data[self.id]

    def serialize(self):
        """Mengubah objek menjadi dictionary/JSON"""
        return {"id": self.id, "name": self.name, "email": self.email}

    def deserialize(self, data):
        """Mengubah dictionary menjadi objek Account"""
        try:
            self.name = data["name"]
            self.email = data["email"]
        except KeyError as error:
            raise DataValidationError(f"Invalid Account: missing {error.args[0]}")
        return self

    @classmethod
    def all(cls):
        """Mengembalikan semua data account"""
        return [account.serialize() for account in cls.data.values()]

    @classmethod
    def find(cls, account_id):
        """Mencari account berdasarkan ID"""
        if account_id in cls.data:
            return cls.data[account_id]
        return None