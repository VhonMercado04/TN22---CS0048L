# num = 5
# if num > 0:
#     print("positive number")
#     print("Another statement...")
# elif num == 0:
#     print("zero")
# else:
#     print("Negative Number")

# num2 = 4
# if num2 >= 0:
#     if num2 == 0:
#         print("zero")
#     else:
#         print(num2, " is a positive number")
# else:
#     print(num2, " is a negative number")   

'''
Nested if and while loop
'''
# count = 0
# grade_num= eval(input("How many grade will you enter? "))

# while count < grade_num:
#     grade = int(input("Enter your grade from 0 - 100: "))

#     if grade >= 70:
#         print("Passed")
#         if grade >= 85:
#             print("Award: With honor")
#         elif grade >= 95:
#             print("Award: High honor")    
#         else:
#             print("No award")
#     else:
#         print("Failed")
#     count += 1

'''
Iterating over a list
for variable in sequence:
    #execute code block
'''
# fruits = ["apple","banana","cherry"]
# for fruit in fruits:
#     print(fruit)

'''
Iterating over a string
'''
# message = "Hello World"
# for char in message:
#     print (char)

#range()

# for i in range(5): #Generate numbers form 0 to 4
#     print (i)

# Start / Stop
# for i in range(1,6):
#     print (i)

#range - Start, Stop and Step
# for i in range(1,12,2): #Generate numbers from 0-9 
#     print (i)

#negative Steps
# for i in range(10,0,-1):
#     print(i)

'''
Iterating over a list
'''
# fruits = ["apple","banana","cherry"]
# for i in range(len(fruits)):
#     print (f"Index {i}: {fruits[i]}")

'''
using range with condition statement
'''
# for i in range(1,11): 
#     if i % 3 == 0:
#         continue    #will skip the print and iterate again
#     print(i)

# if True:
#     pass  #will just pass and will go to print
# print ("This is after pass")    

#nested loop with range

# for i in range(3):
#     for j in range(3):
#         print (f"{i}, {j}",end=' ')
#     print()

#range with break
# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)

#range with else 

for i in range (1,11):
    if i==11:
        break
    print(i)
else:
    print ("Loop Completed")
