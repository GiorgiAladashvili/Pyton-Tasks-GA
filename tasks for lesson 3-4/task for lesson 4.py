# N1
""" st = input("Enter a string: ")
st1 = st.encode()   # default utf-8
print(st1)
print("End Task") """

# N2
st = input("Enter a string: ")
st2= st.strip().lower()+" "+'Python'
if 'python' in st2:
    st2 = st2.replace('python','Python')

print(st2)
print("End Task") 

# N3
""" st = input("Enter a string: ")
mid = len(st)//2
newst = st[:mid]
print(newst)
print("End Task") """

# N4
""" import string

st4 = input("Enter a string: ")
has_alpha = False
has_digit = False

valid_chars = string.ascii_letters + string.digits

for char in st4:
        
    if char not in valid_chars:
         print(f"The string contains an illegal character: '{char}'")
             
    if char.isalpha():
            has_alpha = True
    elif char.isdigit():
            has_digit = True
    
if not has_alpha:
        print("The string does not contain any letters")
    
if not has_digit:
        print("The string does not contain any digits")

print("End Task") """

# N5
""" st5 = input("Enter a string: ")
st5 = st5.encode("utf-8") # utf-16 or utf-32
print("byts:", st5)

decoded = st5.decode("utf-8")
print("string:", decoded) """