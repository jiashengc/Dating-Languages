init python:
    class Question: 
        """
        Question class is a model of questions that can be asked by
        the Main Character/User and the Waifu in question.        
        """
        
        # define a question with a set of responses. 
        # qn: question
        # response: array of responses
        # importance
        def __init__(self, qn, responses, importance):
            self.qn = qn
            self.responses = responses
            self.response_weights = {}
            for response in self.responses:
                response.setWeight(responses.index(response)+1)
                response_weights[response] = response.getWeight()
            self.importance = importance
        
        def getImportance(self):
            return self.importance
        
        def getAvailableResponses(self):
            return self.responses

        def __str__(self):
            str = "Question: " + qn + "\n"
            for response in self.response_weights.keys():
                str+="\t " + (self.response_weights.index(response)+1)+". " + response + " (" + self.response_weights[response]+ ")"
