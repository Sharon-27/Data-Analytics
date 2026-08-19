'''
----> Bitwise operator:-
5 ---> 0101
3 ---> 0011
1 ---> 0001
print(5 & 3)

&---> Bitwise and
Example:-
print(5 & 3)

|----> Bitwise or
5 ---> 0101
3 ---> 0011
7 ---> 0111
print(5 | 7)

^ --> Bitwise XOR
5 ---> 0101
3 ---> 0011
6 ---> 0110
print(5 ^ 3)

>> ---> Right shift
5 --> 0101
1 --> 0001
print(5 >> 1)

<< --> Left shift
5 --> 0101
10 --> 1010
print(5 << 1)

----> input formatting:-
-------
Integer:- syntax-- int(input())
Example:-
num =int(input('Enter a 4 digit number:'))
print(num)

Decimal Example:- syntax-- float(input())
c = float(input("Enter any decimal:"))
print(c + 8)

String:-
so = input("Enter a string:")
print(type(so))

List:- syntax:- list(map(int,input())
List---> 1 2 3--> [1,2,3]
example:-
nums = list(map(int,input('Enter some numbers:').split()))
print(nums)

Tuple:- syntax:- tuple(map(int,input())
Example:-
nums = tuple(map(int,input('Enter some numbers:').split()))
print(nums)

Set:-
nums = set(map(int,input('Enter some numbers:').split()))
print(nums)

Using eval keyword:-
data_ = eval(input('enter: '))
print(type(data_))

----> Output formatting:-
name = 'Saasha'
age = 6
print('My name is',name,'age is',age)
print('Hello!',name)

----> f string:-
name = 'Saasha'
age = 6
print(f'My name is {name} and I am {age} years old')
print('Hello!',name)

----> Modules%:-
name = 'Saasha'
age = 6
print(' my name is %s and I am %d years old' %(name,age))

'''
name = 'Saasha'
age = 6
print(' my name is %d and I am %s years old' %(age,name))
print('Hello!',name)

