from pydantic import BaseModel as BM

class GetEnroleAll(BM):
    client_id: str

class EnrolData(BM):
    gym_id: str
    date: str
    months: str