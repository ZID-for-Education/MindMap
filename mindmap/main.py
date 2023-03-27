class Bubble:
    def __init__(self, text):
        self.text = text
        self.sub = []
    
    def addNode(self):
        self.sub.append()

    def searchNode(self, text):
        for i in self.sub:
            if i.text == text:
                return i.text
            else:
                return None
            
    def __str__(self):
        return self.text
    
    