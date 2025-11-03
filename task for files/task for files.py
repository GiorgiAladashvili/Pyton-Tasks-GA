import os

#1

# def create_file(folder_path, file_name):
#     try:
#         os.makedirs(folder_path, exist_ok=True)

#         file_path = os.path.join(folder_path, file_name)

#         with open(file_path, 'w', encoding='utf-8') as file:
#             file.write("")  

#         print(f"File '{file_name}' created successfully in '{folder_path}'")

#     except Exception as e:
#         print(f"Error occurred: {e}")

# create_file("my_folder/", "example.txt")

#2

# def read_file(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()
#             print("File content:")
#             print(content)
#             return content

#     except FileNotFoundError:
#         print("Error: File not found.")
#     except Exception as e:
#         print(f"Error occurred: {e}")

# read_file("my_folder/example.txt")

#3

# def write_or_append_dict(new_data): 
#     try:
#         file_path = "my_folder/example.txt"
#         folder_path = os.path.dirname(file_path)

#         os.makedirs(folder_path, exist_ok=True)

#         if not isinstance(new_data, dict):
#             raise TypeError("Parameter must be a dictionary.")
        
#         if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
#             with open(file_path, 'w',encoding='utf-8') as file:
#                 file.write("chess_players = [\n")
#                 file.write(f"  {new_data},\n")
#                 file.write("]\n")
#             print("🆕 File created and data written.")
        
#         else:
#             with open(file_path, 'rb+') as file:
#                 file.seek(0, os.SEEK_END)
#                 file.seek(file.tell() - 2, os.SEEK_SET)  # უკან ვბრუნდებით "]\n"-ის წინ
#                 file.truncate()  # ვშლით ბოლო "]"-ს

#             with open(file_path, 'a') as file:
#                 file.write(f"  {new_data},\n")
#                 file.write("]\n")

#             print("✅ File updated successfully (data appended).")

#     except TypeError as te:
#         print(f"❌ TypeError: {te}")
#     except Exception as e:
#         print(f"❌ Unexpected error: {e}")

# write_or_append_dict(
#     {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56}
# )

# write_or_append_dict(
#     {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59}
# )

#4 მე-3 დავალების კოდი ანახლებს კონტექსტს ისედაც