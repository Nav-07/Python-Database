class User:
    def __init__(self, mail):
        self.mail = mail

    def json(self):
        return { "mail": self.mail }