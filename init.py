from os import getcwd
import platform, os

def __init__():
  problemnumber = int(input("Enter the problem number: \n >> "))
  foldername = "Problem-No-" + str(problemnumber)
  path = getcwd() + "\\" + foldername

  # creates directory if it does not exist 
  try:
    os.mkdir(path)
  except OSError as e:
    pass
  os.chdir(path)
  files = os.listdir()
  files.sort()
  try:
    last_file = files[-1]
    last_file = last_file[0:-4] + str((int(last_file[-4]) + 1)) + str(".py")
  except IndexError as e:
    last_file = "Approach-No-1.py"
  last_file = path + "\\" + last_file
  file = open(last_file, 'w')
  file.close()

if __name__ == "__main__":
    __init__()