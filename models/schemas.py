from pydantic import BaseModel


class UserChoice(BaseModel):
    choice: str
    