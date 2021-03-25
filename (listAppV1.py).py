"""
Program goals:
3. Pull the values stored at specific indexes
4. Convert input to INTs
5. Put all action in a while loop

"""
import random
myList = []
unique_list = []
 
def mainProgram():
    #Build our while loop
    while True:
        print("Hello, there! Let's work with lists!")
        print("Please choose from options the following options. Type the number of the choice")
        choice = input("""1. Add to a list,
2. Return a value at a list,
3. Add a bunch or numbers!
4. Random Search
5. Linear Search
6. Sort List
7. Print Lists
8. Quit  """)
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            addABunch()
        elif choice == "4":
            randomSearch()
        elif choice == "5":
            linearSearch()
        elif choice == "6":
            sortList(myList)
        elif choice == "7":
            printLists()
          
        else:
            break
    

def addToList():
    print("Adding to a list: Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))
    #we need to think about errors!

def addABunch():
    print("We're gonna add a bunch of numbers to your lists!")
    numToAdd = input("How many new integers would you like to add?  ")
    numRange = input("And how high would you like these numbers to go?  ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is complete!")

def sortList(myList):
    #"myList" is the ARGUMENT this function takes.
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new, sorted list?  Y/N")
    if showMe.lower() =="y":
        print(unique_list)

def randomSearch():
    print(" oH iM sO rAnDom!!!")
    print(myList[random.randint(0, len(myList)-1)])

def LinearSearch():
    print("We're going to go through this list one item at a time!")
    searchValue = input("what are you looking for?    ")
    for x in range(len(myLists)):
        if myList[x] == int(searchValues):
         print("Your item is at index position {}".format(x))

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:    ")
    print(myList[int(indexPos)])

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list o yo want to see? Sorted or un-Sorted?  ")
        if whichOne.lower() == "sorted":
            print(unique_list)

    
if __name__ =="__main__":
    mainProgram()


