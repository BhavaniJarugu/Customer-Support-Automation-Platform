from dataclasses import dataclass

@dataclass
class Customer:
    id:str
    name:str

@dataclass
class Ticket:
    id:str
    subject:str
    status:str

@dataclass
class Conversation:
    customer_id:str
    message:str
