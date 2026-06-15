from fastapi import FastAPI
from schemas import ChatRequest, TicketRequest
from support_service import SupportService

app = FastAPI(title="Customer Support Automation Platform")
service = SupportService()

@app.get("/health")
def health():
    return {"status":"healthy"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {"response": service.respond(req.message)}

@app.post("/ticket")
def ticket(req: TicketRequest):
    return service.create_ticket(req.subject)
