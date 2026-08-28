'''
----> Looping statements:-
1. For loop:-
Definition:_ A for loop is used to iteratee over a sequence or iterable data types

Example:-
nums = [12,3,5,78]
for j in nums:
    print(j)

nums = [12,3,5,78]
for num in nums:
    print(num)------> define this variable at run to store values from iterable datatype


----> else in for loop:-
Definition:- unlike if-else, else block in for statement is executed after completed of all iterations

Example:-
nums = 'python'
for num in nums:
    print(num)
else:
    print('For ended')


----> Control statements:-

  1.Break:-
Definition:- The break stament is used to stop the loop iterate based on the iteration

Example
nums = [1,2,3,4,5,6,7,]
for num in nums:
    print(num)
    if num == 3:
        break


  2.continue:-
Definition:- The continue is keyword is used to skip the current iteration based on the condition

Example:-
nums = [1,2,3,4,5,6,7,8]
for num in nums:
    if num == 5:
        continue
    print(num)


  3.pass:-(
Definition:- A pass is called as space holder, that is used after statements like if, for, else) not to raise any error

Example:-
for j in range(1,11):
    if j == 15:
        print(j)
    else:
        pass
        

-----> based on if statement we can check whether a number is even or odd
example:-
val_ = [1,2,3,4,5,6,7,8,]
for j in val_:
    if j % 2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')


----> Assert:-
Definition:- Assert is a keyword used to check the condition, incase the conddition is false,it will raise the error(AssertionError)

Example:-
age = 15
assert age >= 18, 'Not eligible to vote'
print('your eligible to vote')

---> While loop:-

num = 1
while num < 5:
    print(num)
    num += 1













'''
num = 7
count = 0
for j in range(1, num+1):
    if j % num == 0:
        pass
    print(j)c
