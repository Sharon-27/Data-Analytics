'''
-----> Scope of variables:-

1. Local variable
Definition:- A variable is definied inside the function call it as a local variable, where the variable can only access with in that function
Example:-
def display():
    name = 'Teja'
    print(name)
display()
print(name)



2. Global variable
Definition:- A variable that is defined outside the function call and it can be access anywhere through out the program
Example:-
a = 90
print(a)
def display():
    print(a)
display()
print(a)


--> global keyword:-
Definition:- Global is a keyword used to reaccess new values to variable that was already define outside the function call
Example:-
a = 90
print(a)
def display():
    global a
    a = 10
display()
print(a)


---> passing by value and passing by refrence:-

---> passing bye value:-
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(109)

---> Passing by refrence:-
num = 7
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(num)
              

---> Recursive function:-
Definition:- The function call itself untill the base condition met
Example:-
def Fac(a):
    if a == 0 or a == 1:
        return a
    return a * Fac(a-1)
print(Fac(5))


              






'''
def Fac(a):
    if a == 0 or a == 1:
        return a
    return a * Fac(a-1)
print(Fac(5))
