from sys import argv

script, filename = argv

print(f"We're going to nuke your {filename}. Now's your last chance to save it.")
print(f"If you want {filename} to be nuked, please press RETURN.")
print(f"If you do not want your file name to get nuked, press CTRL C.")
input("What's it gonna be? \n> ")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye, idiot.")
target.truncate()

print("Now we will create a new file from the ashes...")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("We will brand your file with these lines.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it, once and for all.")
target.close()
