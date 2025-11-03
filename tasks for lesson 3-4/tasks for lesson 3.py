# N1
""" num1 = int(input("Enter a int type Number: "))
sum=0
if num1 > 0:
    for i in range(1,num1):
        sum = sum+i

print(sum, end=' ')
print("End Task") """

# N2

""" num2 = int(input("Enter a int type Number: "))

if num2 > 0:
    
    while num2 > 0:
        print(num2)
        num2 = num2-1
print("End Task") """

# N3

""" from random import randint

num = randint(1, 100)
i = 1

print("Was guessed a number between 1 and 100. Guess it...\n")

guess = 0

while guess != num:
  guess = int(eval(input(f"Step #{i}. Your guess: ")))

  if guess > num:
    print("Too great")
  elif guess < num:
    print("Too less")
  
  print()

  i += 1
else:
  print(f"You guessed a number! It was {num}.")

print("\nGame Over!") """

# N4

""" total_sum = 0

while True:
  str1 = input("Enter a Number or sum: ")
  if str1.isnumeric():
    num3= int(str1)
    if num3>0:
      total_sum = total_sum + num3

  elif str1 == "sum":
    print(f"Total sum is {total_sum}")
    break

print("End Task")  """