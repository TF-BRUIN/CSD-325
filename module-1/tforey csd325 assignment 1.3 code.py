# Truman Forey | 10/25/2024 | Module 1.3 Assignment

#
# dummy number just to get program running/testing purposes
bottles = 10

def run_program():
  global bottles
  # i honestly don't know how to check if a user input is an int, float, or string
  # except to do a try-except check with "x = int(x)", I'm sorry if this is painful to look at
  try:
    bottles = input("How many bottles of beer are on the wall? >")
    bottles = int(bottles)
    print("")
    countdown()
  except:
    print("Please enter a valid number.")
    print("")
    run_program()

def countdown():
  global bottles
  if bottles == 0:
    print("Time to buy more beer!")
    return
  elif bottles == 1:
    print(str(bottles) + " bottle of beer on the wall, " + str(bottles) + " bottle of beer.")
    bottles -= 1
    print("Take one down, pass it around, " + str(bottles) + " bottles of beer on the wall.")
    print("")
    # tail recursion to loop this function
    countdown()
  else:
    print(str(bottles) + " bottles of beer on the wall, " + str(bottles) + " bottles of beer.")
    bottles -= 1
    if bottles == 1:
      print("Take one down, pass it around, " + str(bottles) + " bottle of beer on the wall.")
    else:
      print("Take one down, pass it around, " + str(bottles) + " bottles of beer on the wall.")
    print("")
    # tail recursion to loop this function
    countdown()

run_program()







