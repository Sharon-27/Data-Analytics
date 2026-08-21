'''
----> List:-
Definition:- Collection of different datatypes that are separated by commas,and it is represented in square brackets[]

----> List operations:-
1. Indexing:-
-----
positive indexing---- 0
negative indexing---- -1

examples:-

so = [1,2,3,4,5]
print(so[0])

so = [1,2,3,4,'python']
print(so[4][-1])

all_ = [12,[1,'python',[1,4],(78,[67])],['java',78]]
print(all_[1][3][1])

data_=['python',[1,2(90,'details',[67,0]),(78,'student')]]
print(data_[1][2][1][2])


---len
Definition:- the function is used to find the number of items present inside list
Syntax:- len
Example:-
data_= ['python',[1,2(90,'details',[67,0]),(78,'student')]]
print(len(data_))
 


---> Slicing:-
example:-
data_ = [1,2,3,4,5,6,7]
print(data_[2:6])


---> Concatination:-
Example:-
a = [1,2]
b = [3,4]
print(a+b)

---> Methods:-
----1.append:-

DEfinition:- Append method will add new items into list at last index position
Syntax:- variable_name.append(item)
Example:-
a = [1,2]   
print(a)
a.append(3)
print(a)
a.append(4)
print(a)

----- 2.Extend:-
Definition:- Extend will add the items into a list at last index position,but it will give each value as one index insdide the list
Syntax:----- variable_name.extend(items)
Example:-
a = [1,2]
a.extend('python')
print(a)


-------3.pop:-
Deinition:- Pop() is used to remove items from the list and it will delete basede on the index position
Syntax:----- variable_name.pop(index_position)
Example:-
s = [1,2,3,4,'python']
s.pop(3)
print(s)


------> 4.Remove:-
Definition:- It will delete the items based on the value given in it
Syntax:- ----- variable-name.remove(value)
Example:-
m = [5,1,2,3,4,'python']
m.remove('python')
print(m)











'''
m = [5,1,2,3,4,'python']
m.remove('python')
print(m)
