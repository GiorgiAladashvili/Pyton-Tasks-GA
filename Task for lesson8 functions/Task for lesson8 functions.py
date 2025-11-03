#1
""" def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example usage
n = int(input("Enter number: "))
fibonacci(n) """

#2

""" def is_anagram(str1, str2):
    # Remove spaces and make lowercase for fair comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

word1 = input("Enert the first word: ")
word2 = input("Enert the second word:: ")

# Example
if is_anagram(word1, word2):
    print("this is anagram")
else:
    print("thi is not anagram") """

#3
""" def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example
n = int(input("Enter n: "))
print(f"{n} factorial is: {factorial(n)}") """

#4
""" def count_char(text, char):
    return text.count(char)

# Example
text = input("Enter the word: ")
char = input("enter the char: ")

count = count_char(text, char)
print(f"The character '{char}' appears {count} times in the string.") """