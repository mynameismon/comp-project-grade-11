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
  
  files = [f for f in os.listdir(path) if os.isfile(os.join(path, f))]
  files.sort()
  try:
    last_file = files[-1]
    last_file = last_file[0:-3] + str((int(last_file[-3]) + 1)) + ".py"
  except IndexError as e:
    last_file = "Approach-No-1.py"
  last_file = path + "\\" + last_file
  print(last_file)
  file = open(last_file, 'w')
  file.close()

if __name__ == "__main__":
    __init__()