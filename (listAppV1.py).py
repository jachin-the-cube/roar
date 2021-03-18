"""
program goal:
3. pull the values stored at specific indexes
4. convert input to INS's
5.put all action in while loop
6. add an exit option 


"""""
import random

myList = []


def mainProgram():
   #build our while loop
   while True:
      print ("Hello there, lets work with list")
      print ("plese choose from the following options. ty[e the number of the choice")
      choice = input("""1. add to a list,
2. return a value at a list, or type
3. add a bunch of numbers 
4. random Serch 
5. print list
6. to quit   """)
      if choice == "1":
          addToList()
      elif choice == "2":
           indecValue()
      elif choice == "3":
         addABunch()
       elif choice=="4":
       randomSearch()
       elif choice--"5":
          print(mylist)
       else:
           break
def addToList():
   
     print(" adding to a list great choice")
     newItem = input(" type an interger here!  ")
     myList.append(int( newitem))
     #  we need to think about errors 
def addABunch ():
   print (" we're gonna add a bunch of number to your list!")
   numbToAdd = input("how many new intergers would you like to add?  ")
   numRange = input (" how high would you like these numbers to go  ")
   for x range(0, int(numToAdd)):
      myList.append (random.randint 0, int)numRange)))
      print ("you list is complete!")

def randomSearch() :
   print("OH im so RanDoM :)")
   myList[random.randint(0,  len(myList)-1)])
   

def indexValues():
   print("at what index position do you want you want to search?")
   indexpos = input (" type index position here:   ")
   print ( mylist[int(indexpos)])




if__name__=  " main__"
mainProgram()
