import random

def rand_number():
    
    random_number = random.randint(1, 100)
    count = 1
    
    # print (random_number) for debugging or to know the random number to guess
    while True:
        
        print(f"(attempt {count})", end =" ")
        
        guess = int(input("Enter your guess from 1 to 100: "))
        if guess > 100 or guess < 1:
            print("Invalid number!\n")
        
        else:       
            checker = abs(random_number-guess)
            
            if guess > random_number:
                if checker <= 5:
                    print("You are very close!\n")
                elif checker <= 10:
                    print("A little bit high.\n")           
                else:
                    print("Too high!\n")
                count += 1
            
            elif guess < random_number:
                if checker <= 5:
                    print("You are very close!\n")
                elif checker <= 10:
                    print("A little bit low.\n")    
                else:
                    print("Too low!\n")    
                count += 1
            else:
                print(f"\nCongratulations! You guessed the number in {count} attempts!")
                return

while True:
    print("\n==========================")
    print("-- Number Guessing Game --")
    print("==========================")
    print("  1. Play the number guessing game\n  2. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("The game is starting!") 
        rand_number()

    elif choice == 2:
        print("\nExiting program.. Thanks for playing!\n")
        break

    else:
        print("\nInvalid input!")
    


