from DB_Manager import get_user_by_id

class Chat:
    def __init__(self, id: int, user1_id: int, user2_id: int, created_at: str):
        self.id = id
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.created_at = created_at

class ChatDTO:
    def __init__(self, id: int, user1_id: int, user2_id: int, created_at: str):
        self.id = id
        self.username1 = get_user_by_id(user1_id)
        self.username2 = get_user_by_id(user2_id)
        self.created_at = created_at