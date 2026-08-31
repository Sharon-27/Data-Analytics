'''
---> # palindrome program:-
Example:-
words = 'madam'
empty_str = ''
for i in words:
    empty_str = i + empty_str
    print(empty_str)
if empty_str == words:
    print(f"{words} is a palinrome")
else:
    print(f"{words} is not a palindrome")



---> Amstrong number:-
Example:-
num = int(input("Enter a number:"))
length_ = len(str(num))
amstrong_ = 0
for i in str(num):
    amstrong_ = amstrong_ + int(i)**length_
    print(amstrong_)
if amstrong_ == num:
    print(f'{num} is Amstrong number')
else:
    print(f'{num} is not amstrong number')



----> perfect number:-

num = int(input("Enter a number:"))
sum_ = 0
for i in range(1,num):
    if num % i == 0:
       sum_ += i
if sum_ == num:
    print(f'{num} is perfect number')
else:
    print(f'{num} is not a perfect number')



----> Fibonacci series:-
Definition:- Adding of last two digits then that number gives new digits


num = 0
num_2 = 1
print(num,num_2,end=' ')
for i in range(1,10):
    num_3 = num + num_2
    num = num_2
    num_2 = num_3
    print(num_3,end= ' ')





    




'''
num = 0
num_2 = 1
print(num,num_2,end=' ')
for i in range(1,10):
    num_3 = num + num_2
    num = num_2
    num_2 = num_3
    print(num_3,end= ' ')


