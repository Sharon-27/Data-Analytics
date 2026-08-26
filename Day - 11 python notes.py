'''
-----> elif:-
Definition:- elif statement is used to check more possible outcomes or more conditions

Example:-
a = 90
b = 780
c = 670
if a>b and a>c:#90 > 780 and 90 > 67
    print(a)
elif b>a and b>c:# 780 > 90 and 780 > 67
    print(b)
else:
    print(c)

-----> another example:-
num = 7
num_2 = 3
user_opt = int(input('Enter \n1.add \n2.sub \n3.mul \n4.pow:'))
if user_opt ==1:
   print(num + num_2)
elif user_opt == 2:
    print(num - num_2)
elif user_opt == 3:
     print(num * num_2)
else:
    print(num ** num_2)


-------> Nested if:-
Definition:- if inside an if statement is called nested if

Example:-
app_details = {'pin':1234}
import random
user_pass = int(input("Enter your app password:"))
otp = random.randint(1000,9999)
if user_pass == app_details['pin']:
    print('password is correct')
    print(otp)
    user_otp = int(input("enter 4 digit OTP:"))

    if user_otp == otp:
       print('welcome to the app')
    else:
        print('incorrect otp')
else:
        print('password is incorrect')


----> problem solving:-

----> #Checking whether a number is odd or even:-
Example:-
a = int(input("Enter s number:"))
if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')


----> Grading system:-
---- Example:-
marks_ = int(input("Enter you marks:"))
if marks_ >=90:
    print('A+')
elif marks_ >=80:
    print('A')
elif marks_ >=70:
    print('B+')
elif marks_ >=60:
    print('B')
elif marks_ >=50:
    print('C+')
elif marks_ >=40:
    print('C')
else:
    print('Fail')



    


    

'''
marks_ = int(input("Enter you marks:"))
if marks_ >=90:
    print('A+')
elif marks_ >=80:
    print('A')
elif marks_ >=70:
    print('B+')
elif marks_ >=60:
    print('B')
elif marks_ >=50:
    print('C+')
elif marks_ >=40:
    print('C')
else:
    print('Fail')
