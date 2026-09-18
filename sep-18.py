'''
BMI Scenario --> link with Exception handling with usage of while

while <condition>:
    statements(s)...
    ....





while True:
    #Now we are gonna link BMI case to it with exception handling
    try:
        weight = int(input("Enter the weight in kgs:"))
        height = float(input("Emter the height in metres:"))
        if weight > 0 and height > 0:
            #print(weight,height)
            break #it will terminate the loop
            #continue #it skips the current execution and proceed for next
        else:
            print("value must be positive")
    except Exception as e:
        print(e)
bmi = (weight) / ((height)**2)
if bmi<18.5:
        print(f'BMI is {bmi} and you are Underweight --> Eat well')
elif bmi>=18.5 and bmi <=24.9:
    print(f'BMI is {bmi} and you are Healthy --> Keep consistent')
elif bmi >=25 and bmi <=29.9:
    print(f'BMI is {bmi} and you are Overweight -->\
          Start Exercising')
elif bmi>30:
    print(f'{name} is in Obese Category and bmi is {bmi}')
else:
    print("Do enter only +ve values greater than 0")

    

#Task --> for same above scenario accept 10 users input and store the data in dictionary




#File handling:- create files,make some changes over files
#we will use open(),with()--->.txt files
#we have different modes --> 'r','w','a','r+'

#first we will create a.txt file and write some content to it --> 'r'

file = open('sample-python.txt','r')
#print(file)
#now to read content from the file
#print(file.read())
#print(file.readline()) #reads a single line from the file
print(file.readlines()) #returns list of lines



#'w' mode ---> It automatically creates a new line and if same file is existing
#it overrides
file = open('sharon.txt','w')
print(file)
#print(file.read()) #it is not readable
file.write("How are you Saasha")
file.close() #once the file is closed then only the data is written to file


#we can use with keyword
with open('sharon.txt','w') as file:
    #print(file) #in this case we already sharon.txt file the content is overide
    file.write("Love is waste of time")
    file.write("It gives us stress")
    file.write("\nso listen my words")
    #no need for usage of close() content will be directly written



data = ["Codegnan","python","Vizag","DA"]
data.append('\nPFS')
with open('saasha.txt','w') as file:
    #file.write(data) in this case write() fails as it needs only str
    for text in data:
        file.write(text)

with open('leo.txt','w') as file:
    file.writelines(data) #this can directly insert the data from the list



#'a' ---> will create a new file,if file is already existing content will
#be added instead of overiding
with open('leo.txt','w') as file:
          file.write("\n Today we are having webinar related to VoiceAI Agent")


'''
#'r+' ---> performs both read and write operations
with open('leo.txt','r+') as f:
    #print(f.read())
    f.write("\n Webinar is very important") #in this case it starts writing
    #when we use write() first and then read()
    print(f.read())











