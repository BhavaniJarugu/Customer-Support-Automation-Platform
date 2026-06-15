class KnowledgeService:

    def __init__(self):
        self.docs=['Password Reset Guide','VPN Setup Guide']

    def search(self,query):
        return [d for d in self.docs if query.lower() in d.lower()]

    def answer(self,query):
        return f'Knowledge answer for {query}'
