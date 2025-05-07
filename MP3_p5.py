subj_name_list = []
subj_grade_list = []

def Add_grade(name, grade):
    subj_name_list.append(name)
    subj_grade_list.append(grade)
    print(f"\n{name} : {grade} is added to the list")

def calculate_grade():
    
    if len(subj_grade_list) == 0:
        print("\nAdd Subject and Grade First")
        return
    
    ave_grade = 0
    
    for grades in subj_grade_list:
        ave_grade += grades
    
    
    final_grade = (ave_grade/(len(subj_grade_list)))
    print("\n-----------------")
    print("List of subjects:")
    print("-----------------")
    for index, subj in enumerate(subj_name_list):
        print("Subject",(index+1),":",subj)
        
    print("-------------------")
    print("Grade per subjects:")
    print("-------------------")
    for index, sub_grade in enumerate(subj_grade_list):
        print("Your Grade in subject",(index+1),":",sub_grade)
        
    print(f"\nYour average grade in all subjects: {final_grade:.2f}")    
        
while True: 
    print("\n==============================")
    print("-- Student Grade Calculator --")
    print("==============================")

    print("  1. Add score\n  2. Calculate Average\n  3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 3:
        print("\nExiting program... Thank you")
        break
       
    if choice == 1: 
            subject_name = input("Enter subject name: ")
            
            while True:
                subject_grade = int(input("Enter grade: "))
            
                if subject_grade >= 0 and subject_grade <= 100: 
                    Add_grade(subject_name, subject_grade)
                    break
                else:
                    print("Invalid grade!\n")    

    elif choice == 2:
        calculate_grade()

    else:
        print("\nInvalid input!")    
