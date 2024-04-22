from pydantic import BaseModel as BM

class ReviewModel(BM):
    client_id: str
    text: str

class ReviewModel(BM):
    text: str