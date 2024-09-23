# Python Loops
word = 'Python Rocks'
for i in word:
    print(i)  
    if i == "R":  # Check if the current character is 'R'
        print("This is a cool letter!")  

# Loops and Control Statements (continue, break and pass) in Python
   # Break
while True:
    name = input("Enter your name:")
    if name != "":
        break

   # Continue
phone_number = "123-456-789"
for i in phone_number:
    if i =="-":
        continue
    print(i , end="")  
    
   # Pass
for i in range(0,10):
    if i == 13:
        pass
    else:
        print(i)
        
 # Looping technique in python 
# Enumerating over a list of items
for index, value in enumerate(['Python', 'Loops', 'Example']):
    print(f"{index}: {value}")

#zip() 
    questions = ['Your name', 'Your favorite color', 'Your country']
answers = ['John', 'Blue', 'USA']

for question, answer in zip(questions, answers):
    print(f"{question}? {answer}.")      

#sorted() and #reversed()
numbers = [4, 2, 9, 1, 5, 6, 3, 4]
print("The sorted list is:")
for num in sorted(numbers):
    print(num, end=" ")

print("\nThe sorted list without duplicates is:")
for num in sorted(set(numbers)):
    print(num, end=" ")

print("\nThe reversed list is:")
for num in reversed(numbers):
    print(num, end=" ")

#  range vs xrange on python
#range
b = range(10)
print(b)  
print(type(b))

# In Python 2, range() returned a list directly, while xrange() was
#  used to generate numbers lazily (like range() in Python 3).
#  However, in Python 3, there is no xrange(); range() now behaves like the old xrange() from Python 2.


# Programs for printing pyramid technique in python
rows = int(input("Enter number of rows: ")) 

for i in range(rows, 0, -1):  
    for j in range(0, rows - i): 
        print(" ", end="")
    for j in range(0, i):  
        print("* ", end="")
    print()  

# Chaining comparison in python
x = 5
result = 0 < x < 10
print(result)  

x = 15
result = 0 < x < 10
print(result) 

# else with for
for i in range(5):
    print(i)
    if i == 4:
       print("yes")
else:
     print("no")  
     

# switch function
sides = int(input("Enter the number of sides of the shape:\t"))
match sides:
    case 3:
        print("It's a Triangle")
    case 4:
        print("It's a Quadrilateral")
    case 5:
        print("It's a Pentagon")
    case 6:
        print("It's a Hexagon")
    case 7:
        print("It's a Heptagon")
    case 8:
        print("It's an Octagon")
    case _:
        print("Enter a number between 3 and 8")

# Using iteration in python effectively
fruits = ["apple", "banana", "cherry", "mango", "orange"]

for fruit in fruits:
    if fruit == "mango":
        print("Found the mango!")
        continue
    print(fruit)

    
from itertools import product
x = ['a', 'b']
y = [1, 2, 3]
prod = product(x, y)
print("Product object:", prod)
print("List of all combinations (product):", list(prod))

from itertools import combinations
# Using combinations with a list and choosing 3 elements at a time
z = ['apple', 'banana', 'cherry', 'date']
comb = combinations(z, 3)
print("\nCombinations object:", comb)
print("List of all combinations (choosing 3):", list(comb))


# Python iter() and next() | Converting an object into an iterator
# next()
fruits = ["Apple", "Banana", "Cherry", "Date"]
fruit_iterator = iter(fruits)

y = next(fruit_iterator)
print(y)
y = next(fruit_iterator)
print(y)
y = next(fruit_iterator)
print(y)
y = next(fruit_iterator)
print(y)

# iter()
colors = ["Red", "Green", "Blue", "Yellow"]
color_iterator = iter(colors)

print("\nFirst color:", next(color_iterator))

for color in color_iterator:
    print(color)


# Python | Difference between iterable and iterator 
# Iterable example
lst = [3, 4]
for a in lst:
    print('a:', a)
    for b in lst:
        print('b:', b)

# Iterator example
it = iter([3, 4])
for a in it:
    print('a:', a)
    for b in it: 
        print('b:', b)


# Generators in python 
def countdown_generator(n):
    while n > 0:
        yield f"Countdown: {n}"
        n -= 1

if __name__ == "__main__":
    countdown = 3  
    gen_obj = countdown_generator(countdown)

    print(type(gen_obj))  
    print(next(gen_obj))  
    print(next(gen_obj))
    print(next(gen_obj))

# Generators expression in python
lst = (i for i in range(1_001_010))
print(f"{lst._sizeof():} Byte")
