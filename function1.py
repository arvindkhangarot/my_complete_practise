#Defining a Function
#Here’s a simple function named greet_user() that prints a greeting:
# def simple_msg():
#     print('hello')
# simple_msg()

#Passing Information to a Function

# def user1(enter_user_name):
#     print('hello!',enter_user_name)
# user1('ram')
#
# def user(entername):
#     print('how are you',entername)
# user('shyam')

# def favorite_book(title):
#     print(title,'''such as One of my favorite books is Alice in Wonderland''')
#
# favorite_book('english,')


#Passing Arguments
#Positional Arguments
# def describe_pet(animal_type, pet_name):
#     print('i have a',animal_type)
#     print('name of ',animal_type,'is',pet_name)
# describe_pet('dog','john')



# Keyword Arguments
# def describe_pet(animal_type, pet_name):
#     print('i have a',animal_type)
#     print('name of ',animal_type,'is',pet_name)
# describe_pet('dog','john')
# describe_pet(animal_type='hamster', pet_name='harry')

# def student(student_name,game):
#     print('my name is ',student_name)
#     print('my favrat game is',game)
# student(student_name='ram',game='cricket')

#Default Values
# def describe_pet(pet_name, animal_type='dog'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name='willie')

#Because an explicit argument for animal_type is provided, Python will ignore the parameter’s default value.

# def describe_pet(pet_name='aa', animal_type='dog'):
#     print('i have a',animal_type)
#     print('my', animal_type,'name is',pet_name)
# describe_pet(pet_name='kk', animal_type='hh')


# def student(student_name,game):
#     print('my name is ',student_name)
#     print('my favrat game is',game)
# student(game='cricket',student_name='ram')

# def student(name,class1=4):
#     print('my bane is ',name)
#     print(name,'is in class',class1)
# student(name='ram')

# def describe_city(city_name,country='india'):
#     print(city_name ,'is in ',country)
# describe_city('jaipur')

#Return Values
#Returning a Simple Value
# def student(first_name,last_name):
#     full_name=f'{first_name} {last_name}'
#
#     return full_name
# print(student('ram','singh'))

# def student(first_name,middle_name,last_name):
#     full_name=f'{first_name} {middle_name} {last_name}'
#
#     return full_name
# print(student('ram','singh','khangarot'))

#if middle name not provided
# def student(first_name,last_name,middle_name=''):
#     if middle_name:
#         print(f'{first_name}   {middle_name} {last_name}')
#     else:
#         print(f'{first_name} {last_name}')
# print('ram','khangarot')
# print('ram','singh','khangarit')

#Returning a Dictionary
# def student(first_name,last_name):
#     stu= {'first':first_name,'last':last_name}
#     return stu
# print(student('ram','khangarot'))

#extend this function to accept optional values
# def student(first_name,last_name,age=None):
#     stu={'first':first_name,'last':last_name,}
#     if age:
#         stu['age']=age
#
#     return stu
# print(student('ram','singh',age='27'))

# def student(first_name, last_name, age=None,city=None):
#     stu = {'first': first_name, 'last': last_name}
#     if age:
#         stu['age']=age
#         if city:
#             stu['city']=city
#     return stu
# print(student('ram','singh'))
# print(student('ram','singh',age=27))
# print(student('ram','singh',age=27,city='jaipur'))

#Passing a List
# def student(stu_name):
#     for i in stu_name:
#         message ='hello',i
#         print(message)
# stu_name=['ram','shyam','ravi']
# print(student(stu_name))

# def student(stu_name):
#     for i in stu_name:
#         message='how are you',i
#         print(message)
# stu_name=['ram','shyam','ravi']
# print(student(stu_name))


#Passing an Arbitrary Number of Arguments
# def make_pizza(*toppings):
#     print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# def make_pizza(*toppings):
#     print('Making a pizza with the following toppings')
#     """Summarize the pizza we are about to make."""
#     for i in toppings:
#         print(i)
#The function responds appropriately, whether it receives one value or three values:

# print(make_pizza('mushrooms', 'green peppers', 'extra cheese'))

# def student(*clas):
#     print("class 4 student are folling")
#     for i in clas:
#         # print(i)
#
#     return i
# student('rm','shyam','hanuman')

#Mixing Positional and Arbitrary Arguments
# def make_pizza(size,*toppings):
#     print('making a ',size,'-inch pizza with followint topping')
#     for i in toppings:
#         print(i)
# make_pizza(16,'mushrooms', 'green peppers', 'extra cheese')

# def student(clas,school_name,*name):
#     print(clas,'-class student of',school_name,'are folloing')
#     for i in name:
#         print(i)
# name='ram','shyam','hanuman'
# student(4,'nm school',name)

#Using Arbitrary Keyword Arguments ??
# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
# user_profile = build_profile('albert', 'einstein',
# location='princeton',
# field='physics')
# print(user_profile)



# def make_pizza(size, *toppings):
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for i in toppings:
#         print(i)
# import make_pizza

#function of list
# find sum

# a=[1,2,5,8,7,9]
#
# for i in a:
#     sum1 = 0
#     i =i+sum1
#     sum1.append(i)
#
# print(sum1)

# def sum_list(mylist):
#     total = 0
#     for i in range(len(mylist)):
#         total=total+mylist[i]
#     return total
# mylist=[1,2,5,8,7,9]
# print(sum_list(mylist))


# def sum_list(mylist):
#     total=0
#     for i in mylist:
#         total=total+i
#     return total
# mylist=[1,2,5,8,7,9]
# print(sum_list(mylist))

# mylist1=[20,40,32,6,78,90]
# total=0
# for i in range(len(mylist1)):
#     total=total+mylist1[i]
# print(total)

#find max
# mylist1=[20,40,32,6,78,90]
# max=0
# for i in mylist1:
#     if i>=max:
#         max=i
# print(i)

# def number(mylist):
#     max=0
#     min=mylist[0]
#     for i in mylist:
#         if i >=max:
#             max=i
#             for j in mylist:
#                 if j <= min:
#                     min = j
#     return max,min
# mylist1=[20,40,32,6,78,90]
# print(number(mylist1))

# def even_no(mylist):
#     even=[]
#     for i in mylist:
#         if i % 2 == 0:
#             even.append(i)
#     return even
# mylist1=[5,40,32,6,78,91]
# print(even_no(mylist1))
# print(len(even_no(mylist1)))


# find odd no
# def odd_no(mylist):
#     odd=[]
#     for i in mylist:
#         if i % 2 !=0:
#             odd.append(i)
#     return odd
# mylist=[5,40,32,6,78,91,93]
# print(odd_no(mylist))

#Turn every item of a list into its square
# def squre(mylist):
#     sq=[]
#     for i in mylist:
#         i=i**2
#         sq.append(i)
#     return sq
# mylist=[5,40,32,6,78,91,93]
# print(squre(mylist))

##remove empty list(none)

# def remove_none(mylist):
#     result=list(filter(None,mylist))
#     return result
# mylist = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# print(remove_none(mylist))

#find max key of value
sum of key and value
count positive not
count negative no
average of list
multiply aal list element

max key max value
dict mai value dalna










