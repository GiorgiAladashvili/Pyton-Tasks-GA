#1
""" int_list = [10,20,30,40]
def func_add_list(x):
    int_list.append(x)

func_add_list(50)
print("New list:",int_list) """

#2

""" def sum_of_list(numbers):
    return sum(numbers)

nums = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
print("The sum of the list:", sum_of_list(nums)) """

#3

""" gl_str = "Global"

def show_local():
    gl_str = "Local"
    return gl_str

print("Global variable:", gl_str)
print("Local variable from function:", show_local()) """

#4
""" def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_digits(number // 10)

num = int(input("Enter a number: "))
print("The sum of digits:", sum_of_digits(num)) """

#5
""" def reverse_string(text):
    if len(text) == 0:
        return text
    else:
        return text[-1] + reverse_string(text[:-1])
        #text[-1] → takes the last character of the string
        #text[:-1] → takes the string without the last character

st1 = input("Enter a string: ")
print("Reversed string:", reverse_string(st1)) """

#6

def flatten(lst):
    for item in lst:
        if isinstance(item, dict):
            yield from flatten(list(item.values()))
        elif isinstance(item, (list, tuple, set, frozenset)):
            yield from flatten(list(item))
        else:
            yield item

arr = [1, 2, 3, [[4, 5, 6], "Text", 7], {'title': 'The wolf', 'pages': 256}, (8, [9, 0], True, {5, 8, False})]

arr = list(flatten(arr))

print(arr)