class Message:
    def __init__(self, id: int, chat_id: int, sender_id: int, content: str, created_at: str):
        self.id = id
        self.chat_id = chat_id
        self.sender_id = sender_id
        self.content = content
        self.created_at = created_at