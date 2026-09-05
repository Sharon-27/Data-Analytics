'''
----> Modules:-
Definition:- A module is a python file (.py) that written using function,variables,operators,etc.

Example:-

import math
print(math.pow(2,3))


---- Two types:-

1. built-in modules

---- The modules are developed by the programmer and those comes with installation
example:-

1.math
Example:-

import math
print(math.pow(2,3))


2.os
Example:-

import os
print(os.getcwd())



3.sys
Example:-

import sys
print(sys.path)
print(sys.version)
print(sys.path)



4.random
Example:-

import random
print(random.randint(1000,9999))


5.date and time

2. user-defined modules

---> immporting specific function from the module
syntax:----> from module import function

Example:-

from NEW_FILE import add_
print(add_(90,7))



---> Using Alias name:-
--- Syntax:---> import module as alias name

Example:-

import NEW_FILE as python
print(python.add_(90,7))


---> * using:-

Example:-

from NEW_FILE import *
print(add_(90,7))
print(sub(90,7))














'''
from NEW_FILE import *
print(add_(90,7))
print(sub(90,7))




