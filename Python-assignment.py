'''
Assignment--1

----> create a nested dictionary using codegnan portal as example

using:- List, set, dictionary, tuple

'''
codegnan={
    "Weekly Classes":('Monday','Tuesday','Wednesday',
            'Thursday','Friday','Saturday'),
#created a tuple
    "Learning Topics":['Python','Aptitude','Softskills','MySQL'],
#created a list
    "Project Demos":{'Email Spam Detection',
                     'ATM Management System'},
#created a set
    "Mock Interviews":{
        'Technical Round':8,
        'HR Round':9,
        'Communication Round':8},
#created a dictionary
}
print(codegnan["Weekly Classes"])
print(codegnan["Learning Topics"])
print(codegnan["Project Demos"])
print(codegnan["Mock Interviews"])
