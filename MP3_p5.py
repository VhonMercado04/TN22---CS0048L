subj_name_list = []
subj_grade_list = []
final_grade = 0
ave_grade = 0
def Add_grade(name, grade):
    subj_name_list.append(name)
    subj_grade_list.append(grade)
    print(name,":",grade,"is added to the list")

def calculate_grade():
    global final_grade
    global ave_grade
    for grades in subj_grade_list:
        ave_grade += grades

    if len(subj_grade_list) == 0:
        print("\nAdd Subject and Grade First")
    
    else:
        final_grade = (ave_grade/(len(subj_grade_list)))
        print(final_grade)    
        
while True: 
    print("\n==============================")
    print("-- Student Grade Calculator --")
    print("==============================")

    print("  1. Add score\n  2. Calculate Average\n  3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 3:
        print("Exiting program... Thank you")
        break

    if choice == 1: 
        subject_name = input("Enter subject name: ")
        subject_grade = int(input("Enter grade: "))
        Add_grade(subject_name, subject_grade)

    elif choice == 2:
        calculate_grade()

    else:
        print("Invalid input")    