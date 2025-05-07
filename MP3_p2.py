
def cel_to_fah(cel):
    fah_res = ((cel * 9)/5)+32
    return float(fah_res)

def fah_to_cel(fah):
    cel_res = ((fah - 32)*5)/9
    return float(cel_res)

while True:
    print("\n====================")
    print("-- Converter menu --")
    print("====================")

    print("  1. Celcius to Fahrenheit\n  2. Fahrenheit to Celsius\n  3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 3:
        print("\nExiting the program... Thank you\n")
        break
    
    if choice == 1:
        celsius = float(input("Enter Temperature in Celsius: "))
        print("Temperature in Fahrenheit: ",cel_to_fah(celsius))
    
    elif choice == 2:
        fahrenheit = float(input("Enter Temperature in Fahrenheit: "))
        print("Temperature in Celsius: ",fah_to_cel(fahrenheit))
    
    else:
        print("invalid input...")


