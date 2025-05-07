num1 = 0
num2 = 0

def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b
    
def div(a,b):
    return a/b   

while True:
    print("=====================")
    print("-- Calculator menu --")
    print("=====================")
    print("  a. Add\n  b. Subtract\n  c. Multiply\n  d. Divide\n  e. Exit")

    choice = input("Enter your choice: ")

    if choice == "e":
        print("\nExiting the program.. Thank you\n")
        break
    
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    if choice == "a":
        print("\nThe sum of",num1,"and",num2," is :", add(num1,num2),"\n")
    
    elif choice == "b":
        print("\nThe difference between", num1, "and", num2, " is :", sub(num1,num2),"\n")

    elif choice == "c":
        print("\nThe product of", num1, "and", num2, "is :", mul(num1,num2),"\n")

    elif choice == "d":
        if num2 == 0:
            print("\nError! Number 2 should not be 0\n")
        else:
            print("\nThe quotient of", num1, "and", num2, "is :", div(num1,num2),"\n")

    else:
        print("\nInvalid input!")

    
