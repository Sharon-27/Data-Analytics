'''
-----> Strings:-
data which is presented with in the quotations is known as strings (sequence of characters)
example:- 'python', '1,2', ','


-----> String operations:-

1. Indexing:-
---- Indexing is used to get char that you looking to access
and we have two types of indexing:-
1. positive indexing

---Positive indexing starts from 0 Index
----- Syntax:- print(variable_name[index_position])
example:-
text = 'python'
print(text[4])

2.negative indexing

---- Negative indexing starts with -1 index
----Syntax:- print(variable_name[negative index_position])
Example:-
text = 'python'
print(text[-1])

---- len()
Definition:- len() is built in function that is used get number of char present in the string
---Syntax:- len(variable_name)
Example:-
text = 'python is a programming language'
print(len(text))


----> Slicing:-
Definition:- The slicing is use to access the particular part from the string
Syntax:- variable_name[start:end]
Example:-
text = 'python is a programming language'
print(text[12:23])
print(text[12: ])
print(text[:23])
print(text[::])

----> Upper()
Definition:- upper() is used to convert all small char into capital form
Example:-
text = 'python is a programming language'
print(text.upper())


---->Lower()
Definition:- Lower() is used to convert all cap into small
Example:-
text = 'PYTHON' 
print(text.lower())


----> Index:-
Deinition:- Index is used to know the index position of an char
Syntax:- variable_name.index('substring', start,end)
Example:-
text = 'python is a programming language' 
print(text.index('i'))
print(text[7])


----> Replace:-
Defnition:- Replace is used to replace old substring with new substring
Syntax:- variable_name.replace(old,new)


-----> Split:-
Deinition:- Split menthod is used to separate the string based on the given substring
Example:-
text = 'python is a programming language' 
print(text.split(' '))


-----> Count:-
Definition:- It is used to count the number of occurences of an substring
Syntax:- variable_name.count('substring')
Example:-
text = 'python is a programming language' 
print(text.count('a',1,12))












'''
text = 'python is a programming language' 
print(text.count('a',1,12))


