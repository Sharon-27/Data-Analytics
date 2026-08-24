'''
Set:-
Definition:- Set is unordered collection of elements
        ----> No duplicates allowed in the set
        ----> set is represented by {}


Example:-

nums = {1,2,3,2,}
print(nums)


---->Set operations:-

1. Union:-
Definition:- the union() will combine two sets into a single set
---> syntax:-set_1.union(Set_2) or set_1 | set_2

example:-
data_ = {1,2,3,4,}
nums = {5,6}
print(data_.union(nums))
print(data_ | nums)


2. Intersection:-
Definition:- this will gives us the common elements from both sets
-----> syntax:- set_1.intersection(set_2) or set_1 & set_2

Example:-
data_ = {1,2,3,4,}
nums = {4,5,6}
print(data_.intersection(nums))
print(data_ & nums)


3. Difference:-
Definition:- it will display the different elements from set_1,but no the set_2 elements
----->syntax:- set_1.difference(set_2) or set_1

Example:-
data_ = {1,2,3,4,}
nums = {4,5,6}
print(nums.difference(data_))

another example:-
data_ = {1,2,3,4,}
nums = {4,5,6}
print(data_.difference(nums))


4. symmetric difference:-
Definition:- different elements from the both
synatx:- set_1.symmetric_difference(set_2) or set_1 ^ set_2


Example:-
data_ = {1,2,3,4}
nums = {3,4,5,6}
print(data_.symmetric_difference(nums))
print(nums ^ data_)


-----> Set methods:-
   1. Add:-
   DEfinition:- add() method will add only one element at a time
   Syntax:- set.add(elements)
   
 Example:-
data_ = {1,2,3,4}
print(data_)
data_.add(7)
print(data_)


   2. update:-
   Definition:- we can add more than one elements by using update method
   --> syntax:- set.update([elements]) or set_1.update(set_2)

Example:-
data_ = {1,2,3,4}
nums = {4,5,6}
print(data_)
data_.update([8,9])
print(data_)
data_.update(nums)
print(data_)


   3. Remove:-
   Definition:- remove method will delete the given element from the set, if the element is not present it will raise error
   ---> syntax:- set.remove(element)

Example:-
data_ = {1,2,3,4}
data_.remove(3)
print(data_)
data_.remove(5)

    4. Discard:-
    Definition:- The method is used to delete the values from the set, but it never throws any error even the element not inside the set
    syntax:- set.discard(element)

Example:-
data_ = {1,2,3,4}
data_.discard(7)
print(data_)
data_.discard(1)
print(data_)


     5. clear:-
     Definition:- The method is used to delete all elements from the set and it will return empty set
     ---> syantax:- set.clear()

Example:-
data_ = {1,2,3,4}
print(data_)
data_.clear()
print(data_)








'''
data_ = {1,2,3,4}
print(data_)
data_.clear()
print(data_)
