



"""
Program goals:
1. Get input from the user (at multiple stages)
2. Convert some, but not all, inputs to ints from strings.
3. We need to provide the user with choices:
    a. Add more values to a list
    b. Return a value at a specific index position
4. Add search algorithms to program:
    a. Random Search
    b. Linear Search
    c. Binary Search (2 types)
    
"""

"""
the diffrence i have made with this code is a text to speech this code willspeech to you in the beginning to have a good  interaction


this import fuction dowloads a file for text to speech (pyttx3)
it runs an engine that lets me puts in a engine.say that i could put my chosin script

voices makes it so i can chage the change the voice in to a female or a male
"""
"""
import random imports a module that contains many option for the random generater
the my list and unique list makes it able for you to make a list and use the moduel to pick a random iton from the list 
"""
import random
myList = []
unique_list = []
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, there  i am E F P F    emmanuels favorite program function i will be your guide today. now Let's work with lists")
engine.runAndWait()
"""VOICE"""
   #getting details of current voice
#changing index, changes voices. 1 for female


voices = engine.getProperty('voices')      
engine.setProperty('voice', voices[1].id)  
engine.setProperty('voice', voices[1].id)   

engine.say("Please choose from the following options. Type the number of the choice")
engine.runAndWait()



import random
myList = []
unique_list = [] 
"""
this function runs a while true statment because it runs in a loop forever 
"""

def mainProgram():
    #Build our while loop
    while True:
            print("Hello, there! Let's work with lists!")
            print("Please choose from the following options. Type the number of the choice")
            choice = input("""1. Add to a list,,
2. Add a bunch or numbers,
3.Get an item at an index
4. Sort List
5. Random Search
6. Linear Search
7. Recursive Binary Search
8. Iterative Binary Search
9. Print List
10. Quit  """)
"""
this is a else ,if, and elif libary. this is where the user reads his options and what ever he seclects that option comes up connect to a fuction from the functiokn libary

they have to press a command  and it runs thar program 

"""


                                if choice == "1":
                                         addToList()
                                elif choice == "2":
                                         addABunch()
                                elif choice == "3":
                                        indexValues()
                                elif choice == "4":
                                       sortList(myList)
                                elif choice == "5":
                                       randomSearch()
                                elif choice == "6":
                                      linearSearch()
                                elif choice == "7":
                                    binSearch = input("What number are you looking for?  ")
                                    recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
                                elif choice == "8":                   
                                    binSearch = input("What number are you looking for?  ")
                                    result = iterativeBinarySearch(unique_list, int(binSearch))
                                if result != -1:
                                    print("Your number is at index position ()".format(result))
                                else:
                                    print("Your number is not found in that list, bud!")
                                 elif  choice == "9":
                                    printLists()
                                else:
                                                breakpoint
                        engine.say("What number are you looking for? ")


"""
this is the fuction libary. these functions are conects to the commands above
they select a function and that runns along with the import modules so that the ciode will run 
"""

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

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:    ")
    print(myList[int(indexPos)])

def randomSearch():
    print(" oH iM sO rAnDom!!!")
    print(myList[random.randint(0, len(myList)-1)])
    if len(unique_list) > 0:
        print(unique_list[random.randint(0, len(unique_list)-1)])

def LinearSearch():
    print("We're going to go through this list one item at a time!")
    searchValue = input("what are you looking for?    ")
    for x in range(len(myLists)):
        if myList[x] == int(searchValues):
         print("Your item is at index position {}".format(x))

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see? Sorted or un-Sorted?  ")
        if whichOne.lower() == "sorted":
            print(unique_list)


#binary search inner workings
"""
Binary search is an efficient algorithm for finding an item from a sorted list of items.
It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one


Recursion is when a statement in a function calls itself repeatedly. The primary difference between
recursion and iteration is that recursion is a process, always
applied to a function and iteration is applied to the set of instructions which we want to get repeatedly executed.
"""

            
def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("Your number is at index position {}".format(mid))
            return mid

        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid -1, x)

        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here!")

def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1

        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1



if __name__ =="__main__":
    mainProgram()
