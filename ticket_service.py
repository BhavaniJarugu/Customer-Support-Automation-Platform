class TicketService:

    def create(self,subject):
        return {
            'ticket_id':'INC1001',
            'subject':subject,
            'status':'Open'
        }

    def close(self,ticket_id):
        return {'ticket_id':ticket_id,'status':'Closed'}

    def assign(self,ticket_id,group):
        return {'ticket_id':ticket_id,'group':group}
