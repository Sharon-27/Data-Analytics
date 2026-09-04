'''
----> Lambda function:-
Definition:- lambda function is small anonymous function
---> lambda can take n number arguments, but only with one expression
---> The function is defined by using lambda keyword
Synatax:-
lambda arguments : expression

Example:-
add_ = lambda a,b,c : a+b+c
print(add_(10,20,9))

----using lambda function checking whether a number is even or odd:-

even = lambda num : num % 2 == 0
print(even(7))

---> using lambda function checking which number is greatest

great_ = lambda a,b : a if a>b else b
print(great_(10,20,))

---> by using lambda function printing cube number

num = lambda a : a**5
print(num(5))

---> Filters()
definition:- filter function will perform only on selected elements of iterables
syntax:- filter(lambda arguments: expression, iterable)

Example:-
nums = [1,2,3,4,5]
data_ = filter(lambda a: a%2==0,nums) 
print(list(data_))


---> Map()
Definition:- The map function will perform on all elements of an iterable
syntax:- map(lambda argumentd: expression,iterable)
nums = [1,2,3,4,5]
get_ = map(lambda a: a+6,nums)
print(list(get_))


--->Reduce()
Definition:- The reduce function repeatedly applies a function to the elements and reduces them to one final value.
---> it is available in the functools module.
Syntax:- reduce(lambda arguments: expression, iterable)

Example:-
from functools import reduce
nums = [1,2,3,4,5]
get_ = reduce(lambda a,b: a+b,range(1,10))
print(get_)








'''
from functools import reduce
nums = [1,2,3,4,5]
get_ = reduce(lambda a,b: a+b,range(1,10))
print(get_)
