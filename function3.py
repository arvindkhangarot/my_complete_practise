#Print the word lucky inside s
# s = "My lucky number is %d, what is yours?"
# print(s[3:8])

#type dete
# d='date is %d/%d/%d' % (17,7,2023)
# print(d)

# Make a program that asks a phone number
# number = input("Enter number: ")
# print('your no is:'+number)


# def sum(mylist):
#     sum=0
#     for i in mylist:
#         sum=sum+i
#     return sum
# mylist = [1,2,3,4,5]
# print(sum(mylist))

#Display all states starting with the letter A
# states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut']
# for i in states:
#     if i[0]=='A':
#         print(i)
# states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut']
# def sts(states):
#     a=[]
#     for i in states:
#         if i[0]=='A':
#             a.append(i)
#     return a
# print(sts(states))


# Display all states ending  with the letter a
# states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut']
# for i in states:
#     if i[-1]=='a':
#         pr int(i)
# s = "Hello World"
# slices = s.split(" ")
# print(slices[1])

# def describe_pet(pet_name, animal_type='dog'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name='willie',animal_type='ff')

# find max key of value
# write max key value in new dict{ 5 : 'ERP"}
# rhen enter in list of dict [{5:'ERP'}]
#
# 1 sum of keys
#                                  find lenth of list
#                                  list element lenth
#                                  find min in negative value
#                                  remove duplicate

# mydict={'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88}
# max= 0
# max_key = None
# for i in mydict.values():
#     if i >= max:
#         max=i
#         max_key=key
# print(max,max_key)

# dictA = {"Mon": 3, "Tue": 11, "Wed": 8}
# def GetKey(val):
#     a=[]
#     for key, value in dictA.items():
#         if val == value:
#             a.append(key)
#     return a

# print(GetKey(11))
# print(GetKey(3))
# print(GetKey(10))

# dict_1 = {100: "python", 200: "Java", 300: "Ruby", 400: "Python", 500: "Python"}
# for i in dict_1:
#     print('key is',i)
# dict_1 = {100: "python", 200: "Java", 300: "Ruby", 400: "Python", 500: "Python"}
# for i in dict_1:
#     print("associate value with key is",dict_1[i])

# dict_1 = {100: "python", 200: "Java", 300: "Ruby", 400: "Python", 500: "Python"}
# for i in dict_1.values():
#     if i =="python":
#         print(i)
# dictA = {"Mon": 3, "Tue": 11, "Wed": 8}
# def get_value(val):
#     a=[]
#     for i ,j in dictA.items():
#         if j==val:
#             a.append(i)
#     return a
#
# print(get_value(11))
# print(get_value(2))

#max value and max key
my_dict = {"Mon": 3, "Tue": 11, "Wed": 8}
def mx_key_value(my_dict):
    my_list=[]
    max_value=0
    max_key=None
    for key,value in my_dict.items():
        if value>=max_value:
            max_value=value
            max_key=key
    my_list=[max_key,max_value]

    return my_list
print(mx_key_value(my_dict))





