'''
---> Functions:-
Definition:- A function is a block of code that can be executed only when it is called..

---> A function start with def keyword and the line is called as definition line,where we can define a function name

---> And if we want to execute the program in the function, need to call with the function name define at def line


Synatx:-

def fun_name(parameters):
    pass
fun_name(arguments)


Example:-
def add_(a,b):
    print(a+b)
add_(5,6)


----> Arguments:-
---> Positional arguments:-
Definition:- The arguments should be same at def line and calling, incase if they are not same number will raise an error

Example:-
def add_(a,b):
    print(a+b)
add_(5,7)


----> Example of fibonacci series using def function:-
num = 0
num_2 = 1
def feb_(num,num_2):
    print(num,num_2,end=' ')
    for i in range(1,10):
        num_3 = num + num_2
        num = num_2
        num_2 = num_3
        print(num_3,end= ' ')
feb_(num,num_2)


---> Default arguments:-
Definition:- The default arguments where the function will only consider the data at calling function even though data present at def line


def feb_(num,num_2):
    print(num + num_2)
feb_([1,3],[5,6])

----
def data_(a=8,b=9):
    print(a+b)
data_(1,2)



----> using def and printing prime number:-
num = int(input("Enter a number:"))
count = 0
def prime(num = 10,count = 1):
    for j in range(1,num+1):
        if num % j == 0:
            count += 1
            print(count)
    if count == 2:
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')
prime(num = int(input("Enter a number:")),count=0)


---> Keyword arguments:-
----
Definition:- Keyword arguments are sending arguments in a pair(a=2), and the passing order is not consider...

Example:-
def data_(age,name,batch,location):
    print(name)
    print(age)
    print(batch)
    print(location)
data_(name='teja',age=45,location='vizag',batch=6)



----> Variable length argument:-
Definition:- Adding a (star * call it as args) before a variable at parameters we can pass tuple of arguments and can be access with indexing
Example:-

def all_(*Name):
    print(Name[4])
all_('Teja','Garikapati','sony','chowdhary','sai')


---> Keyword length arguments:-
Definition:- Adding a ( ** call it as kargs) in parameters and passing the dict at arguments, we can get the output in dict of keys

Example:-
def details(**data_):
    print(data_.keys())
details(Name='Teja',age=45,location='vizag',batch=6)


---> Return keyword:-
Definition:- The return keyword used inside the function, once the return is executed means it will back to calling with return values

Example:-
def all_(a,b):
    return a - b
print(all_(7,9))











    






'''
def all_(a,b):
    return a - b
print(all_(7,9))
