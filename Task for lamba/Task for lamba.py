 #1
import string
def group_elements(list1, list2):
    #result = list(zip(list1,list2))
    result = [str(item) for item in zip(list1, list2)]
    return result

list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c']

result =group_elements(list_1,list_2)

print(f"List 1: {list_1}")
print(f"List 2: {list_2}")
print(f"Zipped Result: {result}")


#2
""" from functools import reduce

def Product_of_elements(list1):
    try:
        return(reduce(lambda x, y: x * y, list1, 1))
    except TypeError as e:
        print(f"Error: Invalid type encountered. {e}")
        print("Please ensure the parameter is a list.")
        return None
    
list_of_numbers = [2, 3, 4, 5]

product_result1 = Product_of_elements(list_of_numbers)
print(f"List: {list_of_numbers}, Product: {product_result1}\n") #120

wrong_input = "mylist"

product_result_2 = Product_of_elements(wrong_input)
print(f"Input: '{wrong_input}', Product: {product_result_2}\n") """

#3

""" get_odds = lambda input_list: list(filter(lambda x: x % 2 != 0, input_list))

list1 = [1, 2, 3, 4, 5, 6, 7]

odd_elements = get_odds(list1)

print(f"Odd Elements: {odd_elements}") """

#4

""" def filter_by_ending(words, ending):
    try:
        if not isinstance(words, list) or not isinstance(ending, str):
            raise TypeError("Invalid parameter types. Expected (list, str).")
        
        result = list(filter(lambda word: isinstance(word, str) and word.endswith(ending), words))
        return result

    except TypeError as te:
        print("TypeError:", te)
    except Exception as e:
        print("An unexpected error occurred:", e)


# Example usage
params = ['hello', 'world', 'coding', 'nod']
ending = 'ing'

print(filter_by_ending(params, ending)) """
