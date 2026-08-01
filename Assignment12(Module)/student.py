# Exercise 2: Create Your Own Module
def calculate_average(marks_list):
    sum = 0
    for i in marks_list:
        sum += i
        i += 1
    average = sum/len(marks_list)
    return average

def find_grade(average):
    if average >= 80:
        return "Grade A+"
    elif average >= 70:
        return "Grade A"
    elif average >= 60:
        return "Grade B"
    elif average >= 50:
        return "Grade C"
    elif average >= 40:
        return "Grade D"
    else:
        return "Fail"

def display_result(name,average,grade):
    print(f"Your name is:{name}")
    print(f"Your marks average is:{average}")
    print(f"Your grade is:{grade}")