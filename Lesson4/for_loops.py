#Create a list of names
from traceback import format_tb

names = ["Alice", "Bob", "Charlie", "David"]

#Iterate for the names list and print every name
for name in names:
    print(name)

################################################

sentence = "Hello, World!"

for character in sentence:
    if character.isalpha(): #check if the character is a letter
        print(character)

numbers = [12, 45, 6, 72, 21, 8, 94, 57]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("The maximum value of this list of numbers is:", maximum)


minimum = numbers[0]

for numb in numbers:
    if numb < minimum:
        minimum = numb

print("The minimum value of this list of numbers is:", minimum)


