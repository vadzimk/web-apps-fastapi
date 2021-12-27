import datetime
from typing import Optional


class User:
    def __init__(self, name, email, password_hash):
        self.id = 1
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.created_data = None
        self.profile_image_url = ""
        self.last_login: Optional[datetime.datetime] = None