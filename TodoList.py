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
    
    def Find(self,stringToSearch):
        for item in self.list:
            if(item == stringToSearch):
                return True
        return False

myListObject = TodoList()

myListObject.Add("test")
myListObject.Add("testsdfgsdfg")

print(myListObject.list)

if(myListObject.Find("test")):
    myListObject.Remove("test")
    print("removed test")

print(myListObject.list)
