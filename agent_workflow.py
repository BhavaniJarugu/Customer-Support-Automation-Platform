class AgentWorkflow:

    def classify(self,message):
        return 'General Inquiry'

    def determine_action(self,message):
        return 'Respond'

    def execute(self,message):
        return {
            'category':self.classify(message),
            'action':self.determine_action(message)
        }
