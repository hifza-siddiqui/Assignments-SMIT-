# Question 1 — Student Profile System
print("=======================================================")
print("\t Question 1 — Student Profile System")
print("=======================================================")
person = {           
    "name" : "Hifza",
    "age" : 16,
    "city" : "Karachi",
    "hobbies" : ["Coding", "painting", "Cooking"],
    "skills" : ["Creative", "Graphic Designing", "Web development"]
}
print("Student Name:", person["name"])
print("First Hobby:", person["hobbies"][0])
print("Skills:", person["skills"])



# Question 2 — Student Marks System
print("=======================================================")
print("\t Question 2 — Student Marks System")
print("=======================================================")

subjects = {        # Nested dictionary 
    "Maths" : {
        "marks" : 73
    },
    "English" : {
        "marks" : 82
    },
    "Science" : {
        "marks" : 56
    },
    "Computer" : {
        "marks" : 59
    } 
}
print("All subjects marks:", subjects)
total_marks = 75 + 100 + 56 + 59
obt_marks = subjects["Maths"]["marks"] + subjects["English"]["marks"] + subjects["Science"]["marks"] + subjects["Computer"]["marks"]
print("Total Marks:", total_marks)
print("Obtained Marks:", obt_marks)
avg = obt_marks/4
print("Average Marks:", avg)



# Question 3 — Grade Checking System
print("=======================================================")
print("\t Question 3 — Grade Checking System")
print("=======================================================")

students = {}                                      #Empty dictionary to store values
students["name"] = input("Enter Your Name: ")      # Taking input from user
students["avg_marks"] = int(input("Enter Your Marks: "))
                                # Condition for checking grade
if students["avg_marks"] >= 80 :
    print("Final Grade: A")
elif students["avg_marks"] >= 70 :
    print("Final Grade: B")
elif students["avg_marks"] >= 60 :
    print("Final Grade: C")
else:
    print("Final Grade: Fail")
                                 # Condition for checking pass or fail 
if students["avg_marks"] >= 60:
    print("Status: Passed....")
else:
    print("Status: Failed...")



# Question 4 — Attendance Management System
print("=======================================================")
print("\t Question 4 — Attendance Management System")
print("=======================================================")

attendence = {          # Nested dictionary
    "total_classes" : {
        "classes" : 27
    },
    "attended_classes" : {
        "attended" : 23
    }
}
attendence_per = (attendence["attended_classes"]["attended"]) / (attendence["total_classes"]["classes"]) * 100      # Calculating Attendence %
print("Attendence percentage:", attendence_per)
if attendence_per < 75:
    print("Stort Attendence.")
else:
    print("Eligible For Exam.")


# Question 5 — Fee Management System
print("=======================================================")
print("\t Question 5 — Fee Management System")
print("=======================================================")

attendence["fee_paid"] = input("Enter Your Fee Status (PAID/UNPAID): ").upper()    #  Taking input
       # Making condition
if attendence["fee_paid"] == "PAID":
    print("Fee Cleared...")
elif attendence["fee_paid"] == "UNPAID":
    print("Fee Pending...")
else:
    print('''Error: Invalid status entered... 
          Only Enter 'Paid' or 'Unpaid''')
    

# Question 6 — Skills Management System
print("=======================================================")
print("\t Question 6 — Skills Management System")
print("=======================================================")

skills = {
    "lst" : ["Creative Writting","Coding", "Graphic Designing", "Cooking"]
}
print("Skills List:", skills["lst"])
skills["lst"].append("Arts & Carft")   # Adding one skill
print("Add one skill:", skills["lst"])
skills["lst"].pop(0)                   # Removing one skill
print("Remove one skill:", skills["lst"])  # Printing updated list
print("TOTAL SKILLS:", skills)


# Question 7 — Login Authentication System
print("=======================================================")
print("\t Question 7 — Login Authentication System")
print("=======================================================")

info = {
    "username" : "hifza",
    "password" : "H@12345"
}       
        # Taking input
username = input("Enter Your Username: ")
password = input("Enter Your Password: ")
if username == info["username"] and password == info["password"]:
    print("Login Successful...")
else:
    print("Invalid Credentials...")


# Question 8 — Address Management System
print("=======================================================")
print("\t Question 8 — Address Management System")
print("=======================================================")

address = {
    "area" : "University road",
    "street" : {
        "num" : "street 4",
        "house_number" : "4/333"
    }
}
address["area"] = "Shah Faisal Colony"
address.update({"zip_code" : 75350})
print("Complete Address:", address)


# Question 9 — Multiple Students Database
print("=======================================================")
print("\t Question 9 — Multiple Students Database")
print("=======================================================")

Students = {
    "student1" : {
        "name" : "Hifza",
        "city" : "Karachi",
        "marks" : "991"
    },
    "student2" : {
        "name" : "Shifa",
        "city" : "Islamabad",
        "marks" : "985"
    }
}
print("Student1 Name:", Students["student1"]["name"])
print("Student2 Marks:", Students["student2"]["marks"])
Students["student1"]["city"] = "Lahore"
print("Student Info:", Students)


# Question 10 — Final Student Report Card System
print("=======================================================")
print("\t Question 10 — Final Student Report Card System")
print("=======================================================")
print("\n\t -----REPORT CARD-----")
#--------------------------- Profile
print("\n__Profile__")     
print("Name:",person["name"])
print("Age:",person["age"])
print("City:",person["city"])
#------------------------Skills
print("Skills", skills["lst"])
#------------------------Address
print("Address:", address)
#---------------------------Marks
print("\n__Result__")      
print("Subjects:",subjects.keys())
print("Total Marks:", total_marks)
print("Obtained Marks:", obt_marks)
percentage = obt_marks / total_marks * 100
print("Percentage:", percentage, "%")
print("Average:",avg)
#-------------------------Grade
if percentage >= 90 :
    print("Grade: A+")
elif percentage >= 80 :
    print("Grade: A") 
elif percentage >= 70 :
    print("Grade: B")
elif percentage >= 60 :
    print("Grade: C")
else:
    print("Grade: Fail")
#-----------------------status
print("\n__Status__")      
if percentage >= 60:
    print("Status: Passed....")
else:
    print("Status: Failed...")
#-------------------------attendence
print("Attendence Percentage:", attendence_per,"%")
#-------------------------Fee Status
print("Fee Status:", attendence["fee_paid"])
