from dataclasses import dataclass

@dataclass
class User:
    email: str
    username: str

@dataclass
class TokenSchema:
    access_token: str
    token_type: str
    expires_in: int
    user: User