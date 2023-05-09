def getList(dict):
    list = []
    for value in dict.values():
        list.append(value)
         
    return list
     
# Driver program
dict = {1:'Geeks', 2:'for', 3:'geeks'}
print(getList(dict))