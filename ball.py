class Ball:
    color=' '
    position=0
    def __init__(self):
        color=0
        position=-1
        
    def __init__(self,colo,posi):
        self.color=colo
        self.position=posi
    
    def getcolor(self):
        return self.color
    
    def getposition(self):
        return self.position
    
    def setcolor(self,colo):
        self.color=colo
        
    def setposition(self,pos):
        self.position=pos
