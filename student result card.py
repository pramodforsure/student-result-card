student_name = input("enter your name :")
python_marks = int(input("enter your python marks:"))
maths_marks = int(input("enter your maths marks:"))
english_marks = int(input("enter your english marks:"))
total = python_marks+maths_marks+english_marks
average = total/3
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"


print("=====student result====")
print(f"Student: {student_name}")
print(f"python marks: {python_marks}")
print(f"maths marks: {maths_marks}")
print(f"english marks: {english_marks}")

print(f"Total: {total}")
print(f"average: {average}")
print(f"grade: {grade}")
