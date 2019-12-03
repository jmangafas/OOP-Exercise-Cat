#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Blacky', 20)
cat2 = Cat('Furry', 10)
cat3 = Cat('Scratchy', 40)

age = [int(cat1.age), int(cat2.age), int(cat3.age)]
age.sort()

#print (cat1.name, cat1.age)
#print (cat2.name, cat2.age)
#print (cat3.name, cat3.age)

# 2 Create a function that finds the oldest cat

def oldest():
   print (f'''The oldest cat is {age.pop(2)} years old''')
oldest()

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
