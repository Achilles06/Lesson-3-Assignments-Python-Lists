from collections import Counter

#1. Python List Transformation
#Task 1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
print(grades)
grades.reverse()
print(grades)

#Task 2 Calculate the average grade and display it.
total_grades = sum(grades)
average_count = len(grades)
total_average = total_grades / average_count

print(total_average)

#Task 3 Replace any grade below 80 with the value Failed
for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "failed"
print(grades)

#2 Advanced List Methods and Identity Operators
# Task 1 
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

both_lists = set(submitted).intersection(attended)

print(both_lists)

#Task 2: Check if the two lists are identical in terms of their content, regardless of order.
identical = Counter(submitted) == Counter(attended)

print(identical)

#Task #: Using list methods, remove any student from the attended list who did not submit their assignment.
attended.remove("Eve")
attended.remove("Frank")

print(attended)

#attended = [student for student in attended if student in submitted]
#print(attended)

#3. Advanced Slicing Techniques
#Task 1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

print(temperatures[7:14])

high_temp = []

#Task 2
for temp in temperatures:
    if temp > 100:
        high_temp.append(temp)

print(high_temp)

#Task 4
temperatures.reverse()
print(temperatures[5:10])

#4. Deep Dive into Python Lists
#Task 1

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

#for i in range.students:
    #student = (students[i], grades[1], activities[i])
    #print(student)

#Task 2
students_approved = []
students_approved.append("John")
students_approved.append("Doe")
students_approved.append("Smith")

print(students_approved)
