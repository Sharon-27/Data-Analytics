'''
Python Tasks:-
---> Date:- 17/09/2026


---if-elif-else programs


--->Grade checker

marks = int(input("Enter the marks"))
if marks < 0 or marks > 100:
        print("Invalid marks entered")
elif marks >= 90:
    print('Grade:A')
    print('Remark:Outstanding!')
elif marks >= 80:
    print('Grade:B')
    print('Remark:Excellent!')
elif marks >= 70:
    print('Grade:C')
    print('Remark:"Good"')
elif marks >= 60:
    print('Grade:D')
    print('Remark:Fair,needs improvement')
elif marks >= 50:
    print('Grade:E')
    print('Remark:Poor,needs serious improvement')
else:
    print('Grade:F')
    print('Remark:Failed,needs to reappear')



----> Even-Odd Checker:-

num = int(input("Enter a number:"))
if num == 0:
    print("Zero is neither even nor odd")
elif num < 0 and num % 2 == 0:
    print("Negative Even Number")
elif num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")




----> Month number using if-elif-else
'''
month = int(input("Enter month number:"))
if month == 12 or month == 1 or month == 2:
    print("Season: Winter")
elif month == 3 or month == 4 or month == 5:
    print("Season: Spring")
elif month == 6 or month == 7 or month == 8:
    print("Season: Summer")
elif month == 9 or month == 10 or month == 11:
    print("Season: Autumn")
else:
    print("Invalid month entered")















