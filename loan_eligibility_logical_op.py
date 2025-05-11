income = int(input("What is your salary: "))
credit = int(input("What is your credit score (out of 900): "))
student = input("Are you a student (Y/N, case sensitive): ") == "Y"

if income > 5000 and credit > 600 and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
