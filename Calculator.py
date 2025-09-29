def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y != 0:      
        return x/y
    else:
        return "error Division by 0"
    
while True:
    print("..Simple Calculato..")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


    choice = int(input("Enter your choice (1-5): "))
    if choice ==5:
        print("Existing Programme")
        break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        print("Result:", divide(num1, num2))
    
    else:
        print("Invalid choice! Please select between 1-5.")
