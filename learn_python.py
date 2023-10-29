#pyhon string method
#\n for new line
#\t for tab

#capitalize()	Converts the first character to upper case
# message='hello world'
# print(message.capitalize())

#casefold()	Converts string into lower case
# message='Hello world'
# print(message.casefold())

#center()	Returns a centered string
# message='Hello world'
# print(message.center(25))

#count()	Returns the number of times a specified value occurs in a string
# message = 'hello world'
# print(message.count('hello'))

# message = 'hello world'
# print(message.count('l'))

#endswith()	Returns true if the string ends with the specified value
# message = 'hello world'
# print(message.endswith('d'))

#startwith
# message = 'hello world'
# print(message.startswith('h'))

#find()	Searches the string for a specified value and returns the position of where it was found
# message = 'hello world'
# print(message.find('o'))

#The format() method formats the specified value(s) and insert them inside the string's placeholder.
#The placeholder is defined using curly brackets:
# The placeholders can be identified using named indexes {price}
# message = "For only {price:2f} dollars!"
# print(message.format(price=78))

#index()	Searches the string for a specified value and returns the position of where it was found

# message = 'hello world'
# print(message.index('l'))

#lower()	Converts a string into lower case
# message='HELLO WORLD'
# print(message.lower())

#upper
# message = 'hello world'
# print(message.upper())

#repalce
# txt = 'hello world'
# print(txt.replace('h','a'))

# message='hello world'
# print(message.replace('hello','wow'))

#replace all l with a
# txt = 'hello world'
# print(txt.replace('l','a'))

#split -return list
# messsge='wlcome to the jungle'
# print(messsge.split())

#coccatenation
# a="hello"
# b='world'
# message=a+ ' '+b
# print(message)

#fstring
# employee='arvind'
# salary='55000'
# print(f'salary of {employee} is {salary}')

#slice
# message='hello world'
# print(message[0:5])
# print(message[:5])
# print(message[0:])
# print(message[-1])
# message='hello world'
# print(message[0])

#for help
# message='hello'
# print(message.lower())
# print(help(str()))
# message='hello'
# print(dir(message))

#topic=Integers and Floats - Working with Numeric Data
# num=3
# print(type(num))
# num=3.0
# print(type(num))

#arithmatic operator
# addition 3+2
# subtraction 3-2
# division 4/2
# miltiplication 3*2
# exponant 3**2
# floor division 3//2
# modulus 2%2 gives reminder
# print(3+2)
# print(3-2)
# print(3/2)
# print(3*2)
# print(3**2)
# print(3//2)
# print(3%2)

#built-in function

#absulate valu
# num=-4
# print(abs(num))

#round
# num=10.78
# print(round(num))

#comparison operator
# equal 3==2
# not equal 3!=2
# greter than 3>2
# less than 3<2
# greater or equal 3>=2
# less or equal 3<=2

#return resulat as a true or false


# num_1='200'
# num_2='100'
# print(num_1+num_2)

# num_1='200'
# num_2='100'
# num_1=int(num_1)
# num_2=int(num_2)
# print(num_1+num_2)

#list
# courses=['science','hindi','math','com sci']
# print(courses)
# print(len(courses))
# print(courses[0:2])
# print(courses[0:3:2])

#add an item in list
#add at end of list
# courses.append('histry')
# print(courses)

#add item at specific index
# courses=['science','hindi','math','com sci']
# courses.insert(0,'histry')
# print(courses)

#extend method-for adding multiple value
# courses=['science','hindi','math','com sci']
# extra_course=['histry','arts','music']
# courses.extend(extra_course)
# print(courses)

#remove items from list
# courses=['science','hindi','math','com sci']
# courses.remove('science')
# print(courses)
# courses.pop()#remove last value
# courses.pop(2)
# print(courses)

#sort
# courses=['science','hindi','math','com sci']
# courses.sort()
# courses.reverse()
# print(courses)

# nums=[1,5,2,8,7,9]
# nums.sort()
# print(nums)
# nums.reverse()
# print(nums)

#sorted function-for not changing originak list
# courses=['science','hindi','math','com sci']
# sorted_list=sorted(courses)
# print(sorted_list)

# min,max ,sum

#find index of value
# courses=['science','hindi','math','com sci']
# print(courses.index('com sci'))

#check value present or not in our list
# courses=['science','hindi','math','com sci']
# print('art' in courses)

#enumarate
# courses=['science','hindi','math','com sci']
# for index,i in enumerate(courses):
#     print(index,i)

# courses=['science','hindi','math','com sci']
# for index,i in enumerate(courses,start=1):
#     print(index,i)

#join method=return list to string
# courses=['science','hindi','math','com sci']#return srting with comma seprated
# courses_str=', '.join(courses)
# courses_str='- '.join(courses)
# print(courses_str)

#null-The None keyword is used to define a null value, or no value at all.
'''None is not the same as 0, False, or an empty string.
None is a data type of its own (NoneType) and only None can be None.'''
# myVariable = None
# print(type(myVariable))

# myVariable1 = None
# myVariable2 = None
# print(myVariable1 is myVariable2)
# print(myVariable1 == myVariable2)

# myVariable1 = None
# # Python if statement
# if myVariable1:
#     # printing
#     print("Condition is True")
# # Python else statement
# else:
#     # printing
#     print("Condition is False")
#op-Condition is False

#dict
#acess dict value
# student={'name':'ram','age':25,'courses':['math','com sci']}
# print(student['name'])
# print(student.get('name'))
# print(student.get('class'))#it return None if key not exist
# print(student.get('class','not found'))#it return not found if key not exist
#add ney key value
# student['phone']='555-555'
# print(student)
#updat value
# student['name']='shyam'
# print(student)
#update multiple value using update method
# student={'name':'ram','age':25,'courses':['math','com sci']}
# student.update({'name':'shyam','age':88,'courses':'hindi'})
# student.update({'name':'shyam','age':88,'courses':['hindi','histry']})
# print(student)

#del key method
# student={'name':'ram','age':25,'courses':['math','com sci']}
# del student['name']
# print(student)

#del using pop
# student={'name':'ram','age':25,'courses':['math','com sci']}
# age=student.pop('age')
# print(age)
# print(student)

#acess key value
# student={'name':'ram','age':25,'courses':['math','com sci']}
# print(student.keys())
# print(student.values())
# print(student.items())

#using for loop
# student={'name':'ram','age':25,'courses':['math','com sci']}
# for key in student:
#     print(key)
# student={'name':'ram','age':25,'courses':['math','com sci']}
# for key,value in student.items():
#     print(key,value)

#if else
# if True:
#     print('contidition is true')

# languange='python'
# if languange=='python':#== is check for equality
#     print('contidition is true')

#comparison
# equal                    ==
# Not equal                !=
# greater than             >
# less than                 <
# greater than or equal     >=
# less than and equal       <=
# object idetify            is

# languange='python'
# if languange=='python':
#     print('language is python')
# else:
#     print('not match')
#
# languange='zava'
# if languange=='python':
#     print('language is python')
# else:
#     print('not match')

#elis satement
# languange='zava'
# if languange=='python':
#     print('language is python')
# elif languange=='zava':
#     print('language is zava')
# else:
#     print('not match')
#
# languange='zavascript'
# if languange=='python':
#     print('language is python')
# elif languange=='zava':
#     print('language is zava')
# elif languange=='zavascript':
#     print('language is zavascript')
# else:
#     print('not match')
#

#boolean operation
# and
# or
# not

# user ='admin'
# logged_in=True
# if user=='admin' and logged_in:
#     print('admin')
# else:
#     print('bad code')
#
# user ='admin'
# logged_in=False
# if user=='admin' and logged_in:
#     print('admin')
# else:
#     print('bad code')
#
# #or
# user ='admin'
# logged_in=False
# if user=='admin' or logged_in:
#     print('admin')
# else:
#     print('bad code')

# user ='admin'
# logged_in=False
# if not logged_in:
#     print('plese log in')
# else:
#     print('welcome')

# difference between object idetify    is and ==
# a=[1,2,3]
# b=[1,2,3]
# print(a==b)
# print(id(a))#id of a ,b is different ogject memory
# print(id(b))
# print(a is b)

# a=[1,2,3]
# b=a
# print(id(a))
# print(id(b))
# print(a is b)#both are same ubject memory
# #same as
# print(id(a)==id(b))

#false value
#false
#None
#zero of any number  type
#any empty sequence   [] ()  ''
#any empty mapping  {}


# condition=False
# if condition:
#     print("evalute to true")
# else:
#     print("evealute to false")
#
# condition=0
# if condition:
#     print("evalute to true")
# else:
#     print("evealute to false")
#
# condition= {}
# if condition:
#     print("evalute to true")
# else:
#     print("evealute to false")


#loop amd itration
# number=[1,2,3,4,5]
# for num in number:
#     if num==3:
#         print('found!')
#         break
#     print(num)
#str="Hello World!"
# number=[1,2,3,4,5]
# for num in number:
#     if num==3:
#         print('found!')
#         continue
#     print(num)

# number=[1,2,3,4,5]
# for num in number:
#     for leter in "abc":
#         print(num,leter)

#Split the string based on space character: " ".
# str="Hello World!"
# result=str.split(" ")
# print(result)

#split the number
# str="101:102:103:201:202"
# result=str.split(':')
# print(result)

# str="Arsenal:0-Chelsea:1;Barcelona:2-Bayern Munich:2"
# result=str.split(';')
# print(result)


