# Exercise 2: Create Your Own Module
import student as s

name = input("Enter your name:")
subjects = int(input("How many subjects marks do you want to enter:"))

marks_list = []
i = 1

while i <= subjects:
    marks = int(input(f"Enter marks of {i} subject:"))
    if marks > 1:
        marks_list.append(marks)
        i += 1
    else:
        print("Zero and Negative number are not allowed")
    

average = s.calculate_average(marks_list)
grade = s.find_grade(average)
result = s.display_result(name,average,grade)
