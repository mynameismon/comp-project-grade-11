from os import getcwd
import os
import mdmaketoc

def __init__():
  problemnumber = int(input("Enter the problem number: \n >> "))
  foldername = "Problem-No-" + str(problemnumber)
  path = getcwd() + "\\" + foldername

  # creates directory if it does not exist 
  try:
    os.mkdir(path)
  except OSError as e:
    pass
  i = 1
  while os.path.exists("Problem-No-" + str(problemnumber) + "\\Approach-No-%s.py" % i):
    i+= 1
  last_file = path + "\\" + "Approach-No-%s.py" % i
  file = open(last_file, 'w')
  file.close()

if __name__ == "__main__":
    __init__()
    mdmaketoc.main()