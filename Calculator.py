helloMessage = 'Hello, dear user of my calculator'
print(helloMessage)
print("Select operation.")
print("1.Add.")
print("2.Subtract.")
print("3.Multiply.")
print("4.Divide.")
# Take input from the user chice
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# This function adds two numbers
def add(num1, num2):
   return num1 + num2
# This function subtracts two numbers
def subtract(num1, num2):
   return num1 - num2
# This function multiplies two numbers
def multiply(num1, num2):
   return num1 * num2
# This function divides two numbers
def divide(num1, num2):
   return num1 / num2
if choice == '1': print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2': print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3': print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4': print(num1,"/",num2,"=", divide(num1,num2))
else: print("Invalid input")
