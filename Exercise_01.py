# Basic Syntax & Variables


print("------------ Syntax and Variable ---------------")
#Variable and Data Types
x = 10 
y = 3.14
name = "Python"
is_active = True
number = [1,2,3,4,5]

#Printing 
print(f"Hello, {name}! x + y = {x + y}")

# Type Checking 
print (type (x), type(y), type(name), type(is_active), type(number))

# ----------------------------------------------------------------------------------------------------------------

print("------------ Conditionals ---------------")

# Conditionals

if x > 5:
    print("x is greater than 5")
    
elif x == 5:
    print ("x is exactly 5")
    
else:
    print("x is less than 5")

# For Loop
print("------------ Loops ---------------")

for num in number: 
    print (num, end=" ")
    
print("For loop Ended")

# While Loops 
count = 0
while count < 5: 
    print(count)
    count += 1
    
print("------------ Function ---------------")

def greet(name): 
    return f"Hello, {name}"
print (greet("Alice"))

print("------------ List & Comprehensions ---------------")
squared = [n**2 for n in number]
print (squared)
print ("List Length >>> " + str(len(squared)))
print("Types:", [type(square) for square in squared])

squared.append(36)
print (f"Appending new item >>> {squared}")

squared.insert(1, 3)
print (f"Inserting at index 1 (2nd item) >>> {squared}")

new_list = [49, 64, 81]
print (f"New List >>> {new_list}")

squared.extend(new_list)
print (f"Extending list >>> {squared}")

squared.remove(64)
print (f"Removing 64 from list>>> {squared}")

squared.pop(1)
print (f"Popping from list at index 1>>> {squared}")
squared.pop()
print (f"Popping last element if pop only>>> {squared}")


print("------------ Dictionary & Comprehension ---------------")
squared_dict = {n: n**2 for n in number}
print(squared_dict)
print("Likewise, you can retrive length of dictionary >>> " + str(len(squared_dict)))
print(f"you get retrieve the value via key vis squared_dict.get(2) >>> {squared_dict[2]}") 
print(f"you get retrieve the value via key vis squared_dict.get(2) >>> {squared_dict.get(2)}") 

#You can also change the items too 
squared_dict[1] = 999
print(squared_dict)
# Or adding a new items to the dictionary
squared_dict[6] = 36
print(squared_dict)
# Checking the key exist
if 6 in squared_dict:
    print("Yes, key 6 exist in this dictionary")
    
# You also can pop it
squared_dict.pop(5)
print(squared_dict)
# popitem works but 3.6 and older will be random
squared_dict.popitem()
print(squared_dict)


print(f"To get dictionary keys >> {squared_dict.keys()}")
print(f"To get dictionary values >> {squared_dict.values()}")

print(f"To retrieve the key:value pairs >> {squared_dict.items()} >>> Output as Tuples")

# Tuples
print("------------ Tuples ---------------")

my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
print("Tuple Length:", len(my_tuple))
print("Accessing Element at Index 2:", my_tuple[2])
print("Tuple Slicing (1:4):", my_tuple[1:4])

# Attempting to modify a tuple (will cause an error if uncommented)
# my_tuple[1] = 99  # Uncommenting this will raise TypeError

# Tuple Packing & Unpacking
a, b, c, d, e = my_tuple
print(f"Unpacked Tuple: {a}, {b}, {c}, {d}, {e}")

# Nested Tuple
nested_tuple = (10, (20, 30), 40)
print("Nested Tuple:", nested_tuple)

# Sets
print("------------ Sets ---------------")

my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Adding elements
my_set.add(6)
print("After adding 6:", my_set)

# Removing elements
my_set.remove(3)
print("After removing 3:", my_set)

# Discarding an element (won't raise error if not found)
my_set.discard(10)
print("After discarding 10 (non-existent):", my_set)

# Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a | set_b)  # or set_a.union(set_b)
print("Intersection:", set_a & set_b)  # or set_a.intersection(set_b)
print("Difference (A - B):", set_a - set_b)  # or set_a.difference(set_b)
print("Symmetric Difference:", set_a ^ set_b)  # or set_a.symmetric_difference(set_b)



print("------------ Exception Handling ---------------")
try: 
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Execution finished.")

print("------------ Class & OOP ---------------")

class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak (self):
        return f"{self.name} makes a sound"
    
dog = Animal("Dog")

print(dog.speak())

print("------------ read file ---------------")

with open ("sample.txt", "w") as file:
    file.write("Hello, World!")

with open ("sample.txt", "r") as file:
    print(file.read())
    
print("------------ Lambda Functions ---------------")
    
add = lambda a, b: a + b
print(add (5,3))

print("------------ End ---------------")
    