# Student Record Program

# Student names and marks
names = ["Rahul", "Priya", "Amit", "Sneha"]
marks = [85, 92, 78, 95]

# Display all student records
print("----- Student Records -----")

for i in range(len(names)):
    print(names[i], "-", marks[i])

# Search for a student
search_name = input("\nEnter student name to search: ")

if search_name in names:
    index = names.index(search_name)
    print("Student found!")
    print("Name:", names[index])
    print("Marks:", marks[index])
else:
    print("Student not found.")

# Find highest score
highest = max(marks)
index = marks.index(highest)

print("\n----- Highest Score -----")
print("Student:", names[index])
print("Marks:", highest)

# Find lowest score
lowest = min(marks)
index = marks.index(lowest)

print("\n----- Lowest Score -----")
print("Student:", names[index])
print("Marks:", lowest)

# Sort students by marks
students = list(zip(names, marks))
students.sort(key=lambda x: x[1], reverse=True)

print("\n----- Students Sorted by Marks -----")

for name, mark in students:
    print(name, "-", mark)