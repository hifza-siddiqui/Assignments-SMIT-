# -------------->>Q1
print("Q1) Write a program to print the length of a list. The list should be passed as a function parameter.")

def length(lst):
    fruit = len(lst)
    print("The length of list is:",fruit)

length(["Mango", "Banana", "Apple", "Orange", "Grapes"])

# -------------->>Q2
print("\nQ2) Write a program to print all the elements of a list in a single line.")

def elements(colors):
    for color in colors:
        print(color, end=" ")

elements(["Red", "Orange", "Green", "Black", "White", "Silver", "Pink", "Golden"])

# -------------->>Q3
print("\n\nQ3) Write a program to find the factorial of a given number (n).")

def fact(i):
    factorial = 1
    for a in range(1, i + 1):
        factorial *= a
    print("Factorial of", i,"is:", factorial)

fact(int(input("Enter Any Number: ")))

# -------------->>Q4
print("\nQ4) Write a program to convert Pakistani Rupees (PKR) into US Dollars (USD).")

def pkr_in_usd(pkr):
    rate = 277.29
    usd = pkr / rate
    print("USD:", round(usd, 2))

pkr_in_usd(float(input("Enter amount in PKR: ")))

# -------------->>Q5
print("\nQ5) Write a program to determine whether a given number is even or odd.")
def even_odd(num):
    if num % 2 == 0:
        print(num,"Is An Even Number...")
    else: 
        print(num,"Is An Odd Number...")

even_odd(int(input("Enter Any Number: ")))
