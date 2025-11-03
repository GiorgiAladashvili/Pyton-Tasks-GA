my_dict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
  ]
}

print("Students ID:")
for student in my_dict.get('students'):   
    id = student['id']
    print(id)

st_id= int(input("airchiet studentis ID: "))

student_info = None

for student in my_dict.get("students"):
    if st_id == student.get("id"):
        student_info = student
        break

if student_info:
    st_name = student_info.get("name")
    st_age = student_info.get("age")
    print(f" ID: {st_id}, Name: {st_name}, Age: {st_age}")
    for subject in my_dict.get("subjects"):
        sb_name = subject.get("name")
        sb_grade = subject["grades"].get(str(st_id), "dont have grade")
        print(f"subject: {sb_name}, grade: {sb_grade}")
else:
    print("Student not found!")
