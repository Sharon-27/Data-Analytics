'''
Tuple:-
------>
Definition:- Tuple is collection of different datatypes that separated by, and represented by parenthesis()
----> It is immutable
----> we can pass a tuple of values that can be assign to the variables, but it should match same number of variables and values inside the tuple
Example:-
name,age,born = ('saasha',6,2020)
print(name)
print(age)
print(born)


Example:-
t = (1,'python',[3,4],(7,9))
print(t)

---> Indexing:-
t = (1,'python',[3,4],(7,9))
print(t[2])

---> Index:-
Definition:- If item is not present in the tuple, it will raise value error
Example:-
t = (1,'python',[3,4],(7,9))
print(t.index('python'))

----> len:-
ExMPLE:-
t = (1,'python',[3,4],(7,9))
print(len(t))

----> Max:-
--- Definition:- used to find out the max value from the tuple
Example:-
so = (57, 89, 78,65)
print(max(so))

---> Min:-
---> Definition:- used to find out the least value from the tuple
Example:-
so = (57, 89, 78,65)
print(min(so))


---> Count:-
----> definition:- used to count an item present in the tuple
example:-
so = (57, 89, 78,65,5,5)
print(so.count(5))

---> Concatination:-
Example:-
so = (57, 89, 78,65)
do = (90, 78, 67, 100)
print(so + do)




'''
so = (57, 89, 78,65)
do = (90, 78, 67, 100)
print(so + do)
