from ticket_service import TicketService

class SupportService:

    def __init__(self):
        self.ticket_service = TicketService()

    def respond(self,message):
        return f'Automated response for: {message}'

    def create_ticket(self,subject):
        return self.ticket_service.create(subject)

    def knowledge_lookup(self,query):
        return f'Knowledge result for {query}'
