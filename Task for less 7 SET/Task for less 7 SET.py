#1 
""" line = input("Enter the list (Separate with spaces):\n")
items = line.split()           # ელემენტების გასპლიტვა
unique_items = set(items)    
print("Unique elements (set):", unique_items)"""

#2
""" line = input("Enter the list (Separate with spaces):\n")
items = line.split()           # ელემენტები გასპლიტვა
unique_items = frozenset(items)   
print("Unique elements (set):", unique_items) """

#3
""" set1 = {19, 28, 20, 15, 15, 15, 12, 25, 28, 28, (12, 36)}
set2 = {15, 12, 12, 25, 30, 30}
print(tuple(set1.union(set2))) """

#4
""" line = input("Enter the list (Separate with spaces):\n")   
numbers = tuple(line.split())
unique_list = list(set(numbers))
print("Unique elements (list):", unique_list) """

#5

""" mylist = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

for name, age in mylist:
    print(f"Name: {name}, Age: {age}") """

#6

""" user_list = ["Irakli", "Giorgi", "Nona", "Oto"]
other_users = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
set1=set(user_list)
set2=set(other_users)
print(set1.intersection(set2)) #irakli """