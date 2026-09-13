'''
----

batch = ['sai','PFS-6','Da-6','saketh','akash','python','anil']
print(batch)

#print(batch[2:6:3]) #first 2:6 ---> skip 2 elements
#print(batch[1:7:-2]) #in this case u will receive empty list
#print(batch[-1:-4:-1]) #in this case we come in reverse order
#print(batch[-1:-4:-2])
#in the above case be careful while applying negative step count

#lets include tuple in above list (Tuples are immutable)
batch.insert(2,("vizag","Hyd","vijayawada"))
print(batch)
#print(len(batch))
#as we have a tuple inside a list
#print(len(batch[2]))
#print(batch[2][:2]) #("vizag","hyd")--(sub indexing)
#print(batch[2][1]) #this returns 'Hyd'---> string
#print(batch[2][::2])#it returns("vizag","vijayawada")
print(batch[2].index('Hyd'))
#index ---> first occurance
#count ---> returns the count of objects
#print(batch[2].count('codegnan'))#returns count as 0
#index will raise error, where as count will return 0

batch.insert(3,['pfs','Da','Jfs'])
print(batch)
#now let us apply some of list functions in above batch list
#print(batch[3])
#print(batch[3][1])
#to convert only Jfs as upper case --> JFS
#batch[3][2] = batch[3][2].upper()
#print(batch[3][2])
#now we wanted to add new course in batch[3] position --> AAA
#batch[3].append('AAA')
#print(batch[3])
#print(len(batch))
print(batch)
batch.remove('akash')
print(batch)
#remove ---> value,pop---> index
batch.pop() #pop by default removes last index value
print(batch)
#batch[2].remove('Hyd') #raises Attribute error
#del batch[2][1] #tuple is immutable so we cant insert/remove
#we want to remove entire data but keep the list as it as --> clear()
batch.clear()
print(batch)
'''

#Let us work on Dictionaries
#dict --> {k:v}, keys must be unique
#keys can be int,float,string,list

details = {}
#print(len(details))
details['batch'] = ['PFS6']
#print(details)
details['course'] = ['python']
#print(len(details))
#print(details)
details['students'] = ['sai','Hema']
#print(details)
#we want to update the dictionary
details.update({'branch':('Hyd','Vizag'),
                'Subjects':{'python','Aptitude','Softskilss'}})
print(details)
print(len(details))
#first always check the type  --> dict --> keys()
#keys(),values(),items()
print(details.keys()) #it returns only keys
details['batch'].extend(['JFS','DA'])
#print(details)
details['students'].extend(['Saasha','lilly'])
print(details) #here key should be checked
details['Subjects'].add('DSA') #set is unique and unordered
print(details)

#Task ---> Details --->List,Set,Dictionary (Use Codegnan portal as example)
#Exams,Mock Interviews,Project Demos

#Push to Github --> Share your link in Whatsapp group

