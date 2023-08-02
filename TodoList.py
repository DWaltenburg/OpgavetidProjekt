class TodoList:
    def __init__(self):
        self.__MAXLISTSIZE = 10
        self.__list = []

    def GetList(self):
        return self.__list
    
    def Add(self, stringToAdd):
        if(len(self.__list) < self.__MAXLISTSIZE):
            self.__list.append(stringToAdd)
        else:
            self.__MAXLISTSIZE *=2
            self.__list.append(stringToAdd)

    def Remove(self, stringToRemove):
        newList = []
        for item in self.__list:
            if(item != stringToRemove):
                newList.append(item)
        self.__list = newList
    
    def Find(self,stringToSearch):
        for item in self.__list:
            if(item == stringToSearch):
                return True
        return False

myListObject = TodoList()

myListObject.Add("test")
myListObject.Add("testsdfgsdfg")

print(myListObject.GetList())

if(myListObject.Find("test")):
    myListObject.Remove("test")
    print("removed test")

print(myListObject.GetList())
