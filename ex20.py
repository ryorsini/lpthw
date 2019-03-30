#Import argv from sys
from sys import argv

#Create the CL inputs
script, input_file = argv

#Create "print_all" as a variable - this prints all the lines in the file
def print_all(f):
    print(f.read())

#"Rewinds" the file so that we start from the beginning
def rewind(f):
    f.seek(0)
#Prints the line # and reads the line in the file.
def print_a_line(line_count, f):
    print(line_count, f.readline())

#Opens the file that was created in argv
current_file = open(input_file)

#Prints line, then all of the lines that are in the file as per the func. we made
print("First let's print the whole file:\n")

print_all(current_file)

#Prints line then "rewinds" to the first byte
print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
