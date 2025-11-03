#1 task
""" my_list = []
  
while True:
    print("\n'a' - დაამატეთ რიცხვი სიაში")
    print("'r' - წაშალეთ რიცხვი სიიდან")
    print("'e' - პროგრამიდან გასვლა")
    print(f"მიმდინარე სია: {my_list}")
    
    user_input = input("გთხოვთ, აირჩიეთ ოპერაცია (a/r/e): ").lower()
    
    if user_input == 'a':
      try:
        num_to_add = int(input("შეიყვანეთ რიცხვი დასამატებლად: "))
        my_list.append(num_to_add)
        print(f"რიცხვი {num_to_add} დამატებულია. ახალი სია: {my_list}")
      except ValueError:
        print("არასწორი შეტანა. გთხოვთ, შეიყვანეთ მხოლოდ რიცხვი.")
        
    elif user_input == 'r':
      try:
        num_to_remove = int(input("შეიყვანეთ რიცხვი წასაშლელად: "))
        if num_to_remove in my_list:
          my_list.remove(num_to_remove)
          print(f"რიცხვი {num_to_remove} წაშლილია. ახალი სია: {my_list}")
        else:
          print(f"რიცხვი {num_to_remove} არ არის სიაში.")
      except ValueError:
        print("არასწორი შეტანა. გთხოვთ, შეიყვანეთ მხოლოდ რიცხვი.")
        
    elif user_input == 'e':
      print("პროგრამა დასრულდა")
      break
      
    else:
      print("არასწორი არჩევანი. გთხოვთ, აირჩიეთ 'a', 'r', ან 'e'.")
 """

#2 task

""" my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

# a. დაბეჭდავს 210-ის ინდექსს

index_210 = my_list_1.index(210)
print(f"index of 210 is : {index_210}")

# b. დაამატებს ბოლო ელემენტში ტექსტს "hello"

my_list_1.append("hello")
print(f"new list: {my_list_1}")

# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას
del my_list_1[1]
print(f"new list: {my_list_1}")

# d. შექმენით ახალი სია my_list_2, რომელსაც ექნება my_list_1-ის მნიშვნელობა,

my_list_2 = my_list_1

my_list_2.clear()

print(f"my_list_1: {my_list_1}")
print(f"my_list_2: {my_list_2}") """

#3 task
""" import re

def validate_phone_number(phone_number):
 
    pattern = r"^\(\d{3}\) \d{3}-\d{3}$"
    
    if re.fullmatch(pattern, phone_number):
        return phone_number
    else:
        return "Invalid format"

# test
print(validate_phone_number("(123) 456-789"))   # true
print(validate_phone_number("(555) 123-456"))   # true
print(validate_phone_number("123-456-7890"))    # Invalid format
print(validate_phone_number("(12) 345-678"))    # Invalid format
print(validate_phone_number("(abc) 123-456"))   # Invalid format
print(validate_phone_number("(123)456-789"))    # Invalid format """