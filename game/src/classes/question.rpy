init python: 
    class Question: 
        """
        Question class is a model of questions that can be asked by
        the Main Character/User and the Waifu in question.        
        """

        # define a question with a set of responses. 
        # qn: question
        # responses: array of responses in order of weighting
        #       responses must be of length 3 in which
        #       first response is 
        def __init__(self, qn, responses, importance):
            self.qn = qn
            self.responses = responses
            self.importance = importance

        
        
