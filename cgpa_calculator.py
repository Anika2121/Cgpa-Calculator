def cgpa():
    cgpa_grade={
        'A':4.0,
        'A-':3.7,
        'B+':3.3,
        'B':3.0,
        'B-':2.7,
        'C+':2.3,
        'C':2.0,
        'C-':1.7,
        'D+':1.3,
        'D':1.0,
        'F':0.0
    }
    total_credit=0
    total_points=0
    n=int(input("Enter number of subjects "))
    for i in range(n):
        credit=int(input("Enter credit of subject {}: ".format(i+1)))
        grade=input("Enter grade of subject {}: ".format(i+1)).upper()
        if grade  not in cgpa_grade:
            print("Invalid grade entered. Please enter a valid grade.")
            return
        total_credit += credit
        total_points += cgpa_grade[grade] * credit
    if total_credit == 0:
        print("No credits entered.")
        return     
   

    cgpa = total_points / total_credit
    print("Your CGPA is: {:.2f}".format(cgpa))

if __name__ == "__main__":
    cgpa()
