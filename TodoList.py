class TodoList:
    def __init__(self):
        self.MAXLISTSIZE = 10
        self.list = []

    def Add(self, stringToAdd):
        if(len(self.list) < self.MAXLISTSIZE):
            self.list.append(stringToAdd)

    def Remove(self, stringToRemove):
        newList = []
        for item in self.list:
            if(item != stringToRemove):
                newList.append(item)
        self.list = newList

myListObject = TodoList()

myListObject.Add("test")
myListObject.Add("testsdfgsdfg")

myListObject.Remove("test")
print(myListObject.list)
