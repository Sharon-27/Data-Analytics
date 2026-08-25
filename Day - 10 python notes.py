'''
---> Dictinory:-
Definition:- dictionary is a collection of key : value pair
        ---> key must be unique and it should be immutble datatype(int,str,tuple)
        ---> dict is represented in {}
  Example:-
  details = {1: 2,
           'name': 'teja',
           (1,2): [1,2]}
print(details)

1. Accessing:-
---->
dict can access by calling key,we will get value from that key
--> syntax:- dict['key']

---> get() method is also used to get the value from that key
---> syntax:- dict.get(key)
Example:-
data_ = {'name':'teja',
         'balance':7000,
         'Adr':1234567897654,
         'PANIC':'GPXBP2890Y'}
print(data_['Adr'])
print(data_.get('PANIC'))


data_ = {'name':'teja',
         'balance':7000,
         'Adr':1234567897654,
         'PANIC':'GPXBP2890Y',
         2:[3,4]}
print(data_['Adr'])
print(data_.get(2))


2. Update:-
Definition:- method is used to update a key, incase if the key is not present inside the dict then it will add that key value
---> Syntax:- dict.update({key:value})

---> There is another way to update a key
syntax:--- dict[key] = value


Example:-
data_ = {'name':'teja',
         'balance':7000,
         'Adr':1234567897654,
         'PANIC':'GPXBP2890Y',
         2:[3,4]}
data_['AC'] = 12345676548
data_.update({'name':'sony'})
data_.update({'ATMPIN':7899})
print(data_)


3. values:-
----> 
Definitiuon:- values() method is used get all the values from the dict
---> syntax:- dict.values()
Example:-
data_ = {'name':'teja',
         'balance':7000,
         'Adr':1234567897654,
         'PANIC':'GPXBP2890Y',
         }
print(data_.values())


4.keys()
----> keys() method is used to get all the key from the dict
----> syntax:- dict.keys()


Example:-
data_ = {'name':'teja',
         'balance':7000,
         'Adr':1234567897654,
         'PANIC':'GPXBP2890Y',
         }
print(data_.keys())


5. items():-
-----> Definition:- The method will get the key:value separated from the dict
-----> syntax:- dict.items()
Example:-
data_ = {'name':'teja',
         'balance':7000,
         'Adr':1234567897654,
         'PANIC':'GPXBP2890Y',
         }
print(data_.items())


6. clear():-
----> Dfinition:- A clear method is used to delete all data from the dictionary
----> synatx:- dict.clear()

example:-
data_ = {'name':'teja',
         'balance':7000,
         'Adr':1234567897654,
         'PANIC':'GPXBP2890Y',
         }
print(data_)
del data_['Adr']
print(data_)

data_.clear()
print(data_)




-----> Conditional statements:-
---> 1. if statement:-
Definition:- if condition become true,then it will execute inside block of code
---> incase it becomes false,then it will never entry inside block

Example:-
age = 19
if age>=18:
    print('Eligible to vote')
print(age)


a = 90
b = 78
if a>b:
    print(a)



2. if-else statement:-
----> Definition:- else for if statement is a fall-back statement, incase if condition is false then else block will execute

Example:-
age = 15
if age>=18:
    print(f'your {age} Eligible to vote')
else:
    print(f'your {age} you have to wait {18-age}')


a = 90
b = 780
if a>b:
    print(a)
else:
    print(b)










'''
age = 15
if age>=18:
    print(f'your {age} Eligible to vote')
else:
    print(f'your {age} you have to wait {18-age}')


a = 90
b = 780
if a>b:
    print(a)
else:
    print(b)

