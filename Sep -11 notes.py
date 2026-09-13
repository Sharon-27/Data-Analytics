'''
---

print("Hello Good morning")
#perform operation as below
a = 15
b = 25
print(a+b)


#Tokens --> Keywords,variables,operators,punctuators,[],(),{}
#variable should not start with number,space,symbolss and also no space between words

batch = ['PFS-6','DA-6']
print(batch)
print(type(batch))
#len()--->  returns the number of items in a collection

print(len(batch))
#IDLE is colorcoding editor (violet --> built-in functions)

#Add 3 more student names into it
#List --> Collection --> append(),extend(),insert()
batch.append('sharon')
print(batch)
batch.append(['saasha','cherry'])#nested list
print(batch)
print(len(batch))

batch = ['PFS-6','DA-6']
print(batch)
batch.append('sharon')
print(batch)
batch.extend(['saasha','cherry'])
print(batch)
batch.insert(0,'leo')#inserts given value at specific index
print(batch)
batch.insert(-1,'python')#inserts gives value before index
print(batch)
print(len(batch))
#INDEXING---> []--- index starts at 0 and ends at len(obj)-1
#also in reverse manner it is -1 to len(obj)

print(batch[0])
print(batch[4])
print(batch[34]) #IndexError---> Length is only 7 we are accessing extra

#Slicing ---> group of values [start:end]
'''
batch = ['PFS-6','DA-6']
print(batch)
batch.append('sharon')
print(batch)
batch.extend(['saasha','cherry'])
print(batch)
batch.insert(0,'leo')#inserts given value at specific index
print(batch)
batch.insert(-1,'python')#inserts gives value before index
print(batch)
#print(len(batch))
#print(batch[0:2])
#print(batch[0:3])
#print(batch[4:6])
#print(batch[2:4])
#last 3 elements --> we prefer negative index values
#print(batch[-3:])
#print(batch[:3])
#print(batch)
#striding --> [start:end:step]
print(batch[::2]) #it skips 1 element from start
print(batch[::3]) #it skips 2 elements from start
print(batch[1:5:2])#first performs batch[1:5] -- then skip 1 element

#tryout --> such kind
print(batch[:7:4])
print(batch[7::4])
print(batch[1::5])
print(batch[1:7:-2])
print(batch[-1:-4:-1])

            
