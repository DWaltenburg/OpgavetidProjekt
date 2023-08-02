class TodoList:
    def __init__(self, list):
        self.MAXLISTSIZE = 10
        self.list = []

    def Add(self,x):
        if(len(self.list) < self.MAXLISTSIZE):
            self.list.append(x)