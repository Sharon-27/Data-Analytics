'''
----> List comprehension:-
Definition:- List comprehension is the short form of synax to create a list

syntax:- [expression loop condition]
syntax:- [expression condition else loop]

Example:-

old_ = (1,2,3,4,5)
new_ = [i for i in old_]
print(new_)


old_ = (1,2,3,4,5)
new_ = [i for i in old_ if i%2==0 ]
print(new_)



---> Nested comprehension:-
--- Definition:- using list comprehension generating list inside list


any_ = [[i*j for i in range(1,6)] for j in range(1,10)]
print(any_)


of = [[1,2,3],
      [4,5,6],
      [7,8,9]]
data_ = [num for i in of for num in i]
print(data_)


--> generator
Definition:- A geneerator is a special function which generates one value at a time 






'''
def all_():
    for j in range(1,10):
        yield j
j = all_()
print(next(j))
print(next(j))
print(next(j))
    



