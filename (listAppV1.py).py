"""
program goal:
3. pull the values stored at specific indexes
4. convert input to INS's
5.put all action in while loop
6. add an exit option 


"""""
myList = []


def mainProgram():
   #build our while loop
   while True:
      print ("Hello there, lets work with list")
      print ("plese choose from the following options. ty[e the number of the choice")
      choice = input("1. add to a list, 2. return a value at a list, or type three to quit   ")
      if choice == "1":
          addToList()
      elif choice == "2":
           indecValue()
      elif choice == "3":
         break
        
def addToList():
     print(" adding to a list great choice")
     newItem = input(" type an interger here!  ")
     myList.append(int( newitem))
     #  we need to think about errors 


def indexValues():
   print("at what index position do you want you want to search?")
   indexpos = input (" type index position here:   ")
   print ( mylist[int(indexpos)])




if__name__=  " main__"
mainProgram()
