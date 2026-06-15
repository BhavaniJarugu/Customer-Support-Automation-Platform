from pydantic import BaseModel

class ChatRequest(BaseModel):
    message:str

class TicketRequest(BaseModel):
    subject:str

class ChatResponse(BaseModel):
    response:str

class TicketResponse(BaseModel):
    ticket_id:str
