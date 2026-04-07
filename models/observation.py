from pydantic import BaseModel

class Observation(BaseModel):
    email_text: str
    sender: str
    urgency: str
    step_count: int