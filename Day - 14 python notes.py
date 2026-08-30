'''
----> program regarding finding the odd numbers
Example:-
ran_= int(input('Enter a number:'))
for j in range(1,ran_+1):
    if j % 2 != 0:
        print(f'{j} is odd ')


----> Finding the even or odd numbers from the list:-
nums = [23,78,97,5]
for j in nums:
    if j % 2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')


----> Finding the vowels through the program:-
words_ = 'python Is A programming Language'
vowels = 'aeiouAEIOU'
count = 0
for i in words_:
    if i in words_:
        if i in vowels:
            count += 1
            print(f'{i} is vowel')
print(count)


----> finding the consonants from the program:-
words_ = input("Enter a word:")
vowels = 'aeiouAEIOU'
count = 0
for i in words_:
    if i not in vowels:
        count += 1
        print(f'{i} is consonants')
print(count)



----> Removing duplicates from the list

digits_ = [1,2,3,1,5,3]
empty_ = []
for i in digits_:
    if i not in empty_:
        empty_.append(i)
print(empty_)


----> checking a duplicates in tuple:-

digits_ = (1,2,3,1,5,3)
for i in tuple(digits_):
    if i in digits_:
        print(f'{i} is a duplicate')
    
    








'''
words_ = ' python is a language '
con_ = words_.split(' ')
for i in words_:
    if i == ' ':
        print(words_)
