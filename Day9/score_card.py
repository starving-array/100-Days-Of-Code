student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    score = student_scores[key]
    grade = ''
    if score<=70:
        grade = 'Fail'
    elif score<=80:
        grade = "Acceptable"
    elif score<=90:
        grade = 'Exceeds Expectations'
    else:
        grade = "Outstanding"
    student_grades[key] = grade
    

# 🚨 Don't change the code below 👇
print(student_grades)