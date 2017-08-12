from qnresponse import QnResponse

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
            self.importance = importance
        
        def getImportance(self):
            return self.importance
        
        def getAvailableResponses(self):
            dict = {}
            for response in self.responses:
                response.setWeight(responses.index(response))
                dict[response] = response.getWeight()
            return dict