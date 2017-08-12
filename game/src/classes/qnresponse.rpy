python init: 
    class QnResponse: 
        """
        Responses are used with responses because I don't know how
        else to assign a weight to responses.
        """
        # Res: is the response string itself
        # Weight: is the assigned weight it holds.
        def __init__(self, res, weight):
            self.res =res
            self.weight = weight
        
        def setWeight(self, weight):
            self.weight = weight

        def getWeight(self):
            return self.weight
        
        def getResponse(self):
            return self.res