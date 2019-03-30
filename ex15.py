#Imports argv from sys
from sys import argv

#Delivers arguments required in command line
script, filename = argv

#Assigns txt to opening file
txt = open(filename)

#Prints "here's your file "xyz.filename":
print(f"Here's your file {filename}:")
#Prints the txt in the file
print(txt.read())

#Asks for user to input the file name again
print("Type the filename again:")
#Assigns input to file_again
file_again = input("> ")

#Assigns the open file to txt_again
txt_again = open(file_again)

#Prints the file's contents
print(txt_again.read())

txt.close()
txt_again.close()
