class User:
    def __init__(self, id: int, username: str, password: str, created_at: str):
        self.id = id
        self.username = username
        self.password = password
        self.created_at = created_at