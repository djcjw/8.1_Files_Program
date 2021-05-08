'''
Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.

Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.

The program should then prompt the user for their name, address, and phone number.

Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user.

Once the data has been written your program should read the file you just wrote to the file system and display the file contents to the user for validation purposes.
'''

import os #import the OS library

print("Welcome to my file processing application!") #welcome message

fileDir = input('Please enter the directory for this user-info text file\n(example: "/Users/mymac/Desktop/")\n: ')
fileName = input('Please enter the name of the text file (example: "myfile.txt")\n: ')
completePath = fileDir+fileName
  
if os.path.isdir(fileDir): #check if file directory exists
  print('Directory Exists')
else:
  print('No such directory exists, so the file will be created in another directory.')
  
if os.path.exists(completePath): #check if complete path exists
  print('Complete path exists')
  print('Complete file path:',completePath)
else:
  print('No such file exists, so a new file will be created.')

#user input variables        
name = input('Please enter your name (First Last): ')
address = input("Please enter your address (num street city state zip): ")
phone = input("Please enter your phone number(example: 555-555-5555): ")

with open(completePath, 'w') as fileHandle: #open file for writing
  fileHandle.write("Thanks for entering your info SUCKA! You are now added to our spam email list!") #write data to file
  fileHandle.write('\n\n') #skipping a couple lines
  fileHandle.write (name)
  fileHandle.write(',') #adding comma separation
  fileHandle.write (address)
  fileHandle.write(',')
  fileHandle.write (phone)
    
print("This is what's in the text file:")     
with open(completePath, 'r') as fileHandle: #open same file for reading
  data = fileHandle.read() #read data from the file
  print(data)
  