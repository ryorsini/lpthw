#i = 0
numbers = []

"""def loop(size):
    i = 0
    while i < size:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")"""

#loop(69)

def scam(beg, end):

    for i in range(beg, end):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

scam(0, 9)

print("The numbers: ")

for num in numbers:
    print(num)
