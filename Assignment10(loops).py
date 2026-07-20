# Using While Loop
print("=============================================")
print("\t\tUsing While Loop")
print("=============================================")

# ------------------->Print numbers from 1 to 100.
i = 1
while i <= 100:
    print(i)
    i += 1

# -------------------->Print numbers from 100 to 1.
i = 100
while i >= 1:
    print(i)
    i -= 1

# --------------------->Print the multiplication table of a number n.
a = int(input("Enter Any Number: "))
i = 1
while i <= 10:
    print(a, "x", i, "=", a*i)
    i += 1

# ----------------------->Print the elements of the following list using a loop.
numbers = [12, 45, 8, 23, 67, 34, 90, 15, 56, 78]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# ------------------------>Search for a number x in this tuple using loop.
numbers = (18, 45, 72, 91, 34, 56, 29, 83, 67, 10)
x = int(input("Enter Any Number(18, 45, 72, 91, 34, 56, 29, 83, 67, 10): "))
i = 0
while i < len(numbers):
    if numbers[i] == x:
        print(x, "is Found at index", i)
        break
    else:
          print("Invalid Number Entered....")
          break
    i += 1

# --------------------------->Write a program to find the sum of first natural numbers.
n = int(input("Enter A Number: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print("Sum of first", n, "Natural Numbers are:", sum)    


# Using For Loop
print("=============================================")
print("\t\tUsing For Loop")
print("=============================================")

# ----------------------------->Print the elements of the following list using a loop.
fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes', 'Peach', 'Cherry', 'Guava',
'Pineapple', 'Watermelon']
for fruit in fruits :
    print(fruit)

# -------------------------------->Search for a string x in this tuple using loop.
cities = ('Karachi', 'Lahore', 'Islamabad', 'Peshawar', 'Quetta', 'Multan', 'Hyderabad',
'Faisalabad', 'Sialkot', 'Sukkur')
x = input("Enter Any City: ").capitalize()
for city in cities:
    if city == x :
        print(x,"is found in this tuple")
        break
    else:
        print("Invalid city entered")
        break

# ----------------------->Write a program to find the factorial of first natural numbers. 
numbers = (1, 2, 3, 4, 5)
factorial = 1
for a in numbers:
    factorial *= a
print("Factorial of first 5 natural numbers:",factorial)

# Using range()
print("=============================================")
print("\t\tUsing range()")
print("=============================================")

# ------------------------>Print numbers from 1 to 100.
for i in range(1,101):
    print(i)

# ------------------------->Print numbers from 100 to 1.
for i in reversed(range(1, 101)):
    print(i)

# -------------------------->Print the multiplication table of a number n
num = int(input("Enter Any Number: "))
for i in range(1,11):
    print(num, "x", i, "=", num*i)
    i += 1
