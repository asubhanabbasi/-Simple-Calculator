'''
Simple Calculator
Calculator will perform operations like:
addition(+), substraction(-), multiplication(*) & division(/)

'''

# Functions
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multiply(x,y):
    return x * y

def division(x,y):
    if not(y==0):
     return x / y
    else:
       print("Error! Division by zero")

# Display Menu
def display_menu():
   print("Select an operation")
   print("1. Add")
   print("2. Subtraction")
   print("3. Multiply")
   print("4. Division")

# User Input
def get_user_input():
   operation = (input("Enter your choice ('1' / '2' / '3' / '4'): "))
   if operation in ['1', '2', '3', '4']:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      return operation, num1, num2
   else:
      print("Entered invalid choice!")
      return None, None, None
   
# Calculations
def perform_calculation(operation, num1, num2):
   if (operation == '1'):
      print(f"{num1} + {num2} = {add(num1,num2)}")

   elif(operation == '2'):
      print(f"{num1} - {num2} = {sub(num1,num2)}")

   elif(operation =='3'):
      print(f"{num1} * {num2} = {multiply(num1,num2)}")

   elif(operation == '4'):
      print(f"{num1} / {num2} = {division(num1,num2)}")

# Loop
while True:
   display_menu()
   operation, num1, num2 = get_user_input()
   if operation:
      perform_calculation(operation, num1, num2)
   another = input("Do you want to run another calculation (yes\ no): ")
   if another.lower() != "yes" :
      break


