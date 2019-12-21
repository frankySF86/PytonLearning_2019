from FightUtilites import FrameAdvCalculator

def greet(message):
    "This function prints a message"
    print(message)

greet("hello python stacks")


def messageAndCount(message, *var_counting):
    print(message)
    for num in var_counting:
            print(num)

messageAndCount("Hello Python")
messageAndCount("Hello Python",1,2,3,4)

print(messageAndCount("Hello Python"))
print(str(45))
t = FrameAdvCalculator(2,4,3)
print(t)
t2 = FrameAdvCalculator(2,7,10)

print(t.isAdvantageous())
print(t2.isAdvantageous())

tup1 = (1,2,4)
print(type(tup1))
print(tup1)
print(tup1[0] + tup1[1])
tup1.count
for value in tup1:
    print(value)

#list examples, list are mutable tuples are not

groceryList = ['eggs','milk','cheese']

#loop
for groceryItem in groceryList:
    print(groceryItem)

print(groceryList[0])
print(groceryList.__len__())
print(len(groceryList))

print("Beer" in groceryList)
groceryList.insert(len(groceryList)+1,"Beer")
for groceryItem in groceryList:
    print(groceryItem)

print(groceryList.__len__())


def filterList(expression, itemList):
    filteredList = []
    for item in itemList:
        if(expression(item)):
            filteredList.append(item)

    return filteredList

itemList = [1,2,3,4,5,6,7,8,10]
filteredList = filterList(lambda item: item > 7, itemList)
map(lambda item: item > 5, filteredList)

print(len(filteredList))

