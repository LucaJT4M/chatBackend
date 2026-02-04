class Chat:
    def __init__(self, id: int, user1_id: int, user2_id: int, created_at: str):
        self.id = id
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.created_at = created_at

class ChatDTO:
    def __init__(self, id: int, user1_id: int, user2_id: int, created_at: str):
        self.id = id
        self.username1 = ""
        self.username2 = ""
        self.created_at = created_at
        self.user1_id = user1_id
        self.user2_id = user2_id