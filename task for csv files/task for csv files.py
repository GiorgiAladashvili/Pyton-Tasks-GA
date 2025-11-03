import csv
import os

#1 
 
# file_path = "my_folder/students.csv"
# os.makedirs(os.path.dirname(file_path), exist_ok=True)

# data = [
#     [1,"giorgi", 20, "89", "math", 10],
#     [3,"nodo", 25, "85", "Geograpi", 8],
#     [2,"zura", 15, "88", "bilogi", 9]
# ]

# # CSV-ის შექმნა და ჩაწერა
# with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
#     writer = csv.writer(csvfile)
    
#     writer.writerow(["id", "name", "age", "grade", "subject_name", "mark"])
    
#     writer.writerows(data)

# print(f"CSV file created at: {file_path}")


# csv ფაილიდან ინფოს ამოღება, დასორტირება და შემდეგ უკან ჩაწერა. 

# file_path = "my_folder/students.csv"

# def sort_by_id():
#     try:
#         with open(file_path, 'r', newline='') as csvfile:
#             reader = csv.reader(csvfile)
#             rows = list(reader)

#         # ჰედერის გამოყოფა
#         header = None
#         if rows and not rows[0][0].isdigit():
#             header = rows[0]
#             data_rows = rows[1:]
#         else:
#             data_rows = rows

#         # ვასორტირებთ id-ის მიხედვით (int-ში გადაყვანით)
#         data_rows.sort(key=lambda x: int(x[0]))

#         # ვწერთ უკან ფაილში
#         with open(file_path, 'w', newline='') as csvfile:
#             writer = csv.writer(csvfile)
#             if header:
#                 writer.writerow(header)
#             writer.writerows(data_rows)

#         print("✅ CSV sorted successfully by id.")

#     except FileNotFoundError:
#         print("❌ File not found! Please check the file path.")
#     except Exception as e:
#         print(f"❌ Unexpected error: {e}")

# sort_by_id()


#2.1

# file_path = "my_folder/students.csv"

# def read_all_students(): # ყველა ჩანაწერის წაკითხვა
#     """Reads and prints all student records from the CSV file."""
#     if not os.path.exists(file_path):
#         print("❌ File not found! Please check the file path.")
#         return

#     try:
#         with open(file_path, 'r', newline='') as csvfile:
#             reader = csv.reader(csvfile)
#             rows = list(reader)

#         if not rows:
#             print("⚠️ The file is empty.")
#             return

#         # ჰედერის არსებობის შემოწმება
#         header = None
#         if rows and not rows[0][0].isdigit():
#             header = rows[0]
#             data_rows = rows[1:]
#         else:
#             data_rows = rows

#         print("\n📋 All Students:")
#         for row in data_rows:
#             print(", ".join(row))

#     except Exception as e:
#         print(f"❌ Error reading file: {e}")

# read_all_students()

# 2.2

# def read_student_by_id(student_id):
#     """Reads and prints a single student's info by ID from the CSV file."""
#     if not os.path.exists(file_path):
#         print("❌ File not found! Please check the file path.")
#         return

#     try:
#         with open(file_path, 'r', newline='') as csvfile:
#             reader = csv.reader(csvfile)
#             rows = list(reader)

#         if not rows:
#             print("⚠️ The file is empty.")
#             return

#         # ჰედერის შემოწმება
#         header = None
#         if rows and not rows[0][0].isdigit():
#             header = rows[0]
#             data_rows = rows[1:]
#         else:
#             data_rows = rows

#         found = False
#         for row in data_rows:
#             if row[0] == str(student_id):
#                 print("\n🎓 Student Info:")
#                 if header:
#                     for h, v in zip(header, row):
#                         print(f"{h}: {v}")
#                 else:
#                     print(", ".join(row))
#                 found = True
#                 break

#         if not found:
#             print(f"❌ Student with id {student_id} not found.")

#     except Exception as e:
#         print(f"❌ Error reading file: {e}")

# read_student_by_id(2)

#3

# from collections import defaultdict

# file_path = "my_folder/students.csv"

# def calculate_average_marks_by_subject():
    
#     if not os.path.exists(file_path):
#         print("❌ File not found! Please check the file path.")
#         return

#     try:
#         with open(file_path, 'r', newline='') as csvfile:
#             reader = csv.reader(csvfile)
#             rows = list(reader)

#         if not rows:
#             print("⚠️ The file is empty.")
#             return

#         # ჰედერის შემოწმება
#         header = None
#         if rows and not rows[0][0].isdigit():
#             header = rows[0]
#             data_rows = rows[1:]
#         else:
#             data_rows = rows

#         # საგნების მიხედვით ქულების დაგროვება
#         subject_marks = defaultdict(list)

#         for row in data_rows:
#             subject = row[4]
#             mark = float(row[5])
#             subject_marks[subject].append(mark)

#         # საშუალო ქულის გამოთვლა
#         print("\n📊 Average marks by subject:")
#         for subject, marks in subject_marks.items():
#             avg_mark = sum(marks) / len(marks)
#             print(f"{subject}: {avg_mark:.2f}")

#     except Exception as e:
#         print(f"❌ Error: {e}")

# calculate_average_marks_by_subject()


#4

# file_path = "my_folder/students.csv"

# def update_student_mark():

#     if not os.path.exists(file_path):
#         print("❌ File not found! Please check the file path.")
#         return

#     try:
#         student_id = input("Enter student ID: ").strip()
#         subject_name = input("Enter subject name: ").strip()
#         new_mark = input("Enter new mark: ").strip()

#         # ვკითხულობთ ყველა მონაცემს
#         with open(file_path, 'r', newline='') as csvfile:
#             reader = csv.reader(csvfile)
#             rows = list(reader)

#         if not rows:
#             print("⚠️ The file is empty.")
#             return

#         # ჰედერის შემოწმება
#         header = None
#         if rows and not rows[0][0].isdigit():
#             header = rows[0]
#             data_rows = rows[1:]
#         else:
#             data_rows = rows

#         updated = False
#         for row in data_rows:
#             if row[0] == student_id and row[4].lower() == subject_name.lower():
#                 row[5] = str(new_mark)
#                 updated = True
#                 break

#         if updated:
#             with open(file_path, 'w', newline='') as csvfile:
#                 writer = csv.writer(csvfile)
#                 if header:
#                     writer.writerow(header)
#                 writer.writerows(data_rows)
#             print("✅ Student mark updated successfully.")
#         else:
#             print("❌ Student or subject not found.")

#     except Exception as e:
#         print(f"❌ Error: {e}")

# update_student_mark()
