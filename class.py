#1.   write a  Python program and find even numbers in a given list [28,49,14,27,20,35,47,58,80,89,90,56]
mylist =[28,49,14,27,20,35,47,58,80,89,90,56]
even_no=[]
for i in mylist:
    if i%2==0:
        even_no.append(i)
        print(i)

mylist =[28,49,14,27,20,35,47,58,80,89,90,56]
def even_no(mylist):
    even_no=[]
    for i in mylist:
        if i%2==0:
            even_no.append(i)
    return even_no
print(even_no(mylist))

# write a  Python program and find odd numbers in a given list [28,49,14,27,20,35,47,58,80,89,90,56]
mylist =[28,49,14,27,20,35,47,58,80,89,90,56]
for i in mylist:
    if i%2  !=0:
        print(i)

mylist =[28,49,14,27,20,35,47,58,80,89,90,56]
def odd_no(mylist):
    odd_no=[]
    for i in mylist:
        if i%2!=0:
            odd_no.append(i)
    return odd_no
print(odd_no(mylist))

#3.write a  Python program and find sum of all numbers in a given list[10,20,30,40]
mylist =[28,49,14,27,90,56]
sum=0
for i in mylist:
    sum=sum+i
print(sum)
mylist = [28, 49, 14, 27, 90, 56]
def sum(mylist):
    sum1=0
    for i in mylist:
        sum1=sum1+i
    return sum1
print(sum(mylist))

#4.write a  Python program and find average value in given list
mylist=[10,90,30,40,80,90]
ave=[]
sum=0
for i in mylist:
    sum=sum+i
    ave= sum / len(mylist)
print(ave)

mylist=[10,90,30,40,80,90]
def average(mylist):
    sum=0
    ave=[]
    for i in mylist:
        sum=sum+i
        ave=sum/len(mylist)
    return ave
print(average(mylist))

#5.write a  Python program and find muiltple all numbers in a given list [2,3,5,7,90,6,5]
list= [2,3,5,7,90,6,5]
multiple=1
for i in list:
    multiple=multiple*i
print(multiple)

list= [2,3,5,7,90,6,5]
def multiple(list):
    multi=1
    for i in list:
        multi=multi*i
    return multi
print(multiple(list))

#6. write a  Python program and find dupicate number in a given list [20,90,49,36,20,46,60,36,46,80,72,80]
list=[20,90,49,36,20,46,60,36,46,80,72,80]
new=[]
dupli=[]
for i in list:
    if i not in new:
        new.append(i)
    else:
        dupli.append(i)
print(new)
print(dupli)

#remove duplicate no
list=[20,90,49,36,20,46,60,36,46,80,72,80]
def remove_duplicate_no(list):
    new_list=[]
    duplicate=[]
    for i in list:
        if i not in new_list:
            new_list.append(i)
        else:
            duplicate.append(i)
    return new_list,duplicate
print(remove_duplicate_no(list))

#7.covert two list into one dictionary, list1 = ["r","n","p","x"],list2 = [10,20,30,40]

list1 = ["r","n","p","x"]
list2 = [10,20,30,40]
dict1=dict(zip(list1,list2))
print(dict1)

list1 = ["r","n","p","x"]
list2 = [10,20,30,40]
def convert_list_dict(list1,list2):
    result=dict(zip(list1,list2))
    return result
print(convert_list_dict(list1,list2))

#8. write a Python program to print all odd numbers in a range
for i in range(1,10,1):
    print(i)
start, end = 4, 19

# iterating each number in list
for i in range(start,end+1):
    if i %2==0:
        print(i,end=" ")
start, end = 4, 19
def odd_no_range(start,end):
    odd_no=[]
    for i in range(start,end+1):
        if i % 2!=0:
            odd_no.append(i)
    return odd_no
print(odd_no_range(start,end))

#9. write a  Python program to print positive numbers in a list. list = [1,2,-5,6,-8,-7,4,,-10,30,50,-9]
list = [1,2,-5,6,-8,-7,4,-10,30,50,-9]
for i in list:
    if i >0:
        print(i)

list = [1,2,-5,6,-8,-7,4,-10,30,50,-9]
def positive(list):
    positive_no=[]
    for i in list:
        if i >0:
            positive_no.append(i)
    return positive_no
print(positive(list))

#10.write a  Python program to print negetive numbers in a list, list =  [10,-2,34,3,-3,4,-5,6,8,-1]
list =  [10,-2,34,3,-3,4,-5,6,8,-1]
for i in list:
    if i <0:
        print(i)

list =  [10,-2,34,3,-3,4,-5,6,8,-1]
def negative_no(list):
    neg_no=[]
    for i in list:
        if i <0:
            neg_no.append(i)
    return neg_no
print(negative_no(list))

#1.write a python program to count all positive number , list = [1,-2,-3,3,4,-5,6,-5,-4,-6,5,9,4,9]
list = [1,-2,-3,3,4,-5,6,-5,-4,-6,5,9,4,9]
pos_count=0
neg_count=0
for i in  list:
    if i >0:
        pos_count+=1
    else:
        neg_count+=1
print(pos_count,neg_count)

list = [1,-2,-3,3,4,-5,6,-5,-4,-6,5,9,4,9]
def count_no(list):
    pos_count=0
    neg_count=0
    for i in list:
        if i >0:
            pos_count+=1
        else:
            neg_count+=1
    return pos_count,neg_count
print(count_no(list))
#12. write a python program to find length of dictionary
dict = { "math": 82, "physics": 67, "hindi":87,"english":70,"history":90}
print(len(dict))
13. write a python program find average value of a dictionary names = {"ritu" : 20, "ridhi" : 30, "nidhi" : 40}
mydict={"ritu" : 20, "ridhi" : 30, "nidhi" : 40}
sum=0
average=[]
for i,j in mydict.items():
    j =sum+j
    sum=j
    average=sum/len(mydict)
print(average)

mydict={"ritu" : 20, "ridhi" : 30, "nidhi" : 40}
def average(mydict):
    sum=0
    ave=[]
    for i,j  in mydict.items():
        j=j+sum
        sum=j
        ave=sum/len(mydict)
    return ave
print(average(mydict))

#14. write a pyton program a find even number in a given dictionary and output will be show in a list
names = {"x":1,"y":2,"z":3,"a":4,"b":5,"c":6}
even_no=[]
for i,j in names.items():
    if j %2==0:
        even_no.append(j)
print(even_no)

names = {"x":1,"y":2,"z":3,"a":4,"b":5,"c":6}
def even_no(names):
    even=[]
    for key,value in names.items():
        if value%2==0:
            even.append(value)
    return even
print(even_no(names))

#15. write a pyton program a find odd number in a given dictionary and output will be show in a list
names  = {"x":1,"y":2,"z":3,"a":4,"b":5,"c":6}
def odd_no(names):
    odd=[]
    for i,j in names.items():
        if j%2 !=0:
            odd.append(j)
    return odd
print(odd_no(names))

#16. wite a python program and find max number in a given dictionary
dict = {"ridhi":18,"nidhi":17,"sidhi":20,"vinni":13}
def max_value(dict):
    max=0
    for key,value in dict.items():
        if value>=max:
            max=value
    return max
print(max_value(dict))

#17. write a python program and find min number in  a given dictionary
dict = {"ridhi":18,"nidhi":17,"sidhi":20,"vinni":13}
def min_no(dict):
    min=None
    min_value=[]
    for i,j in dict.items():
        if min is None or j<min:
            min=j
            i=i
    min_value=[i,j]
    return min,min_value
print(min_no(dict))

#8. write a program and marge two python dictionary into one
dict1 = {"r": 12, 'k' : 13,"n": 10}
dict2 = {"x": 1, "y": 2, "z": 3}
dict2.update(dict1)
print(dict2)


def merge(dict1,dict2):
    dict2.update(dict1)
    return (dict2)

dict1 = {"r": 12, 'k' : 13,"n": 10}
dict2 = {"x": 1, "y": 2, "z": 3}
print(merge(dict1, dict2))


#19.write a python program and find sum_of_dictionary_values
dict = {"r":1,"k":2,"n":3,"s":9,"g":6}
def sum_value(dict):
    sum=0
    for key, value in dict.items():
        value=value+sum
        sum = value
    return sum
print(sum_value(dict))
#20.write a python program and find sum of key and value in pyhton dictionary
dict = {1:2,3:4,5:5,5:10} #same keys.takes last key value
def sum_value(dict):
    sum_val=0
    sum_key=0
    for key, value in dict.items():
        value=value+sum_val
        sum_val = value
        key=key+sum_key
        sum_key=key
    return sum_val
print(sum_value(dict))

#21.write a python program that takesna list of name as input and return a dictionary where the keys are the name and
the values are the lengthof the corresponding names. the program should ignore any names that have a
 length less than 4 charcters.
list = ["ridhi","raghu","raj","sonu","avi"]
def get_name(list):
     a={}
     for i in list:
         if len(i) < 4:
             a[i] = len(i)
     return a
print(get_name(list))




#22find the maximum value and its key in the dictionary and convert in to list

dict = {"Mon": 3, "Tue": 11, "Wed": 8}
def max(dict):
    a={}
    my_list=[]
    max_value=0
    max_key=None
    for key,value in dict.items():
        if value>=max_value:
            max_value=value
            max_key=key
    my_list=[max_key,max_value]
    # a={max_key:max_value}
    a[max_key]=max_value
    return a
print(max(dict))

How to return all list elements of a given length?
def by_size(words,size):
    result = []
    for word in words:
        if len(word)==size:
            result.append(word)
    return result
print(by_size(['a','bb','ccc','dd'],2))



def convert(lst):
    res_dict = {}
    for i in range(0,len(lst),2):
        res_dict[lst[i]]=[i+1]
    return res_dict
lst = ['a', 1, 'b', 2, 'c', 3]
print(convert(lst))
product={
"mystock1":{
    "product":'iphone',
    "price":150000,
    "quantity": 100,
    "instock": "yes"
    },
    "mystock2":{
    "product":"airphone",
    "price": 38888,
    "quantity": 100,
    "instock": 'no',
    }
}
# # key find i phone price and stock also
# print(product['mystock1']['product'],product['mystock1']['price'],product['mystock1']['instock'])

#add in dict

dict1={0: 10, 1: 20}
dict1[2]=3
print(dict1)

dict1={0: 10, 1: 20}
dict1.update({2:30})
print(dict1)

#Write a Python script to concatenate the following dictionaries to create a new one.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dict4={}
# for i in (dic1,dic2,dic3):
#     dict4.update(i)
# print(dict4)

#check given key present in dict
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#check key 6 present or not
# if 6 in d:
#     print('yes')

# dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(key):
#     if key in dict:
#         print("key is present")
#     else:
#         print('key is not present')
# is_key_present(1)

'''Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}'''
# n=int(input("Input a number "))
# d = {}
# for i in range(1,n+1):
#     d[i]=i*i #d[i] is key and i*i is value
# print(d)
import random

'''Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
and the values are the square of the keys.'''
# start=1
# end=15
# result_sequre={}
# for i in range(start,end+1):
#     result_sequre[i]=i*i
# print(result_sequre)

#add two dict
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d1.update(d2)
# print(d1)

#10. Write a Python program to sum all the items in a dictionary.
# exam_mark={'histry':30,'hindi':85,'science':52,'arts':88}
# sum=0
# for key,value in exam_mark.items():
#     sum = value+sum
# print(sum)

#multiply value
# my_dict = {'histry':30,'hindi':85,'science':52,'arts':88}
# multi=1
# for i,j in my_dict.items():
#     multi=multi*j
# print(multi)

#Write a Python program to remove a key from a dictionary.
# my_dict = {'histry':30,'hindi':85,'science':52,'arts':88}
# my_dict.pop('histry')
# my_dict.__delitem__('histry')
# print(my_dict)

#using del
# my_dict = {'histry':30,'hindi':85,'science':52,'arts':88}
# if 'hindi' in my_dict:
#     del my_dict['hindi']
# print(my_dict)

#Write a Python program to map two lists into a dictionary.
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# dict1=dict(zip(keys,values))
# print(dict1)

#Write a Python program to get the maximum and minimum values of a dictionary.
# my_dict = {'histry':30,'hindi':85,'science':52,'arts':88}
# max_value=0
# min=None
# min_value=[]
# for i ,j in my_dict.items():
#     if min is None or j<=min:
#         min=j
#         min_value.append(min)
# print(min_value)

# remove duplicate from dict
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#                 }
# result={}
# for key,value in student_data.items():
#     if value not in result.values():
#         result[key]=value
# print(result)

#Write a Python program to check if a dictionary is empty or not.
# mydict={}
# if not bool(mydict):
#     print('dict is empty')
# else:
#     print('not empty')

#Write a Python program to count the values associated with a key in a dictionary.

# student = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# print(sum(d['id'] for d in student))
# print(sum(d['success'] for d in student))
#convert list in to dict value is length
# num_list = [1, 2, 3, 4]
# new_dict = {}
# for name in num_list:
#     new_dict[name] = len(num_list)
#
# print(new_dict)

#use of enumarte
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for index,(key,value) in enumerate(dict_num.items(),start=1):
#     print(index,key,value)

# @remove none form dict
# dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}
# without_None={}
# for key ,value in dict1.items():
#     if value is not None:
#         without_None[key]=value
# print(without_None)

'''42. Write a Python program to filter a dictionary based on values.
Original Dictionary:Marks greater than 170:'''
# mydict={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# markks={}
# for key,value in mydict.items():
#     if value>170:
#         markks[key]=value
# print(markks)

# student_id = ["S001", "S002", "S003", "S004"]
# student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
# for x,y in zip(student_id,student_name):
#     print(x,y)

#convert two list in dict
# test_keys = ["Rash", "Kil", "Varsha"]
# test_values = [1, 4, 5]
# res = {}
# for key in test_keys:
#     for value in test_values:
#         res[key] = value
#         test_values.remove(value)
#         break
# print(res)

# test_keys = ["Rash", "Kil", "Varsha"]
# test_values = [1, 4, 5]
# result=dict(zip(test_keys,test_values))
# print(result)

#clear dict value
# dictionary = {
#                'C1' : [10,20,30],
#                'C2' : [20,30,40],
#                'C3' : [12,34]
#              }
# for key in dictionary:
#     dictionary[key].clear()
# print(dictionary)
#find key in list if value given in dict
#in new dict and new list
# students = {
#   'Theodore': 19,
#   'Roxanne': 20,
#   'Mathew': 21,
#   'Betty': 20
# }
# list1=[]
# list_key=[]
# dict1={}
# val=20
# for key,value in students.items():
#     if value==val:
#         key=key
#         list_key.append(key)
#         dict1[key]=value
#     list1=[key,value]
# print(list1)
# print(dict1)
# print(list_key)

'''78. Write a Python program to create a flat list of all the keys in a flat dictionary.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Create a flat list :'''
# mydict={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# mylist=[]
# for i in mydict:
#     mylist.append(i)
# print(mylist)

# mydict={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# mylist=list(mydict.keys())
# print(mylist)

'''79. Write a Python program to create a flat list of all the values in a flat dictionary.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Create a flat list of all the values of the said flat dictionary:
[19, 20, 21, 20]'''
# mydict={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# mylist=[]
# for i,j in mydict.items():
#     mylist.append(j)
# print(mylist)

# mydict={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# mylist=list(mydict.values())
# print(mylist)

'''80. Write a Python program to find the key of the maximum value in a dictionary.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
Finds the key of the maximum and minimum value of the said dictionary:
('Roxanne', 'Theodore')'''
# mydict={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# min=None
# min_value=

#sort key of dict
# myDict = {'ravi': 10, 'rajnish': 9,
#         'sanjeev': 15, 'yash': 2, 'suraj': 32}
# mykey=list(myDict.keys())
# mykey.sort()
# sorted_key={}
# for i in mykey:
#     for key,value in myDict.items():
#         sorted_key[i] = value
# print(sorted_key)

#sort dict by value??
# myDict = {'ravi': 'ran', 'rajnish': 'shyam'
#         }
# myvalue=list(myDict.values())
# myvalue.sort()
# sorted_value={}
# for i  in myvalue:
#     for key,value in myDict.items():
#         sorted_value[key]=i
# print(sorted_value)

#dictionary with multiple inputs for keys
# data = {
#     (1, "John", "Doe"): {"a": "geeks", "b": "software", "c": 75000},
#     (2, "Jane", "Smith"): {"e": 30, "f": "for", "g": 90000},
#     (3, "Bob", "Johnson"): {"h": 35, "i": "project", "j": "geeks"},
#     (4, "Alice", "Lee"): {"k": 40, "l": "marketing", "m": 100000}
# }
#
# # Accessing the values using the keys
# print(data[(1, "John", "Doe")]["a"])
# print(data[(2, "Jane", "Smith")]["f"])
# print(data[(3, "Bob", "Johnson")]["j"])
#
# data[(1, "John", "Doe")]["a"] = {"b": "marketing", "c": 75000};
# data[(3, "Bob", "Johnson")]["j"] = {"h": 35, "i": "project"};
# print(data[(1, "John", "Doe")]["a"]);
# print(data[(3, "Bob", "Johnson")]["j"])


# Python code demonstrate the working of
# sorted() with lambda
# list = [{"name": "Nandini", "age": 20},
#         {"name": "Manjeet", "age": 20},
#         {"name": "Nikhil", "age": 19}]
#
# # using sorted and lambda to print list sorted
# # by age
# print("The list printed sorting by age: ")
# print(sorted(list, key=lambda i: i['age']))
#
# # print("\r")
#
# # using sorted and lambda to print list sorted
# # by both age and name. Notice that "Manjeet"
# # now comes before "Nandini"
# print("The list printed sorting by age and name: ")
# print(sorted(list, key=lambda i: (i['age'], i['name'])))
#
# # print("\r")
#
# # using sorted and lambda to print list sorted
# # by age in descending order
# print("The list printed sorting by age in descending order: ")
# print(sorted(list, key=lambda i: i['age'], reverse=True))

#create dict ,list as key and no of occurace as a value
# est_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
# dict1={}
# for i in est_list:
#     dict1[i]=est_list.count(i)
# print(dict1)

#nested dict

# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
#           }
# for i,j in people.items():
#     print(i,j)

#find name and age of key 1
# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
#           }
# print(people[1]['name'],people[1]['age'])

#find name and sex of key 2
# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
#           }
# print(people[2]['name'],people[2]['sex'])


# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male',4:[2,3,5]},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
#           }
# sum=0
# if 4 in people[1]:
#     for i  in people[1][4]:
#         sum=sum+i
# print(sum)
#find value of first element key 4 in key 1
# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male',4:[2,3,5]},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
#           }
# print(people[1][4][0])


# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male','course':{1:'english',2:'comsci',3:'histry'}},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
#           }
# print(people[1]['course'][1])


# add elements in a nested dictionary
# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
# people[3]={}
# people[3]['name'] = 'Luna'
# people[3]['age'] = '24'
# people[3]['sex'] = 'Female'
# people[3]['married'] = 'No'
#
# print(people)

#chabge name is luna in key 1
# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
# people[1]['name']='luna'
# print(people)

# Add another dictionary to the nested dictionary
#add {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'} as key 4 value

# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
# people[4]={'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
# print(people)

# delete elements from a nested dictionary
# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
#           3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
#           4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}
# del people[1]['sex']
# del people[2]['sex']
# del people[3]['married']
# del people[4]['married']
# print(people)

# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
#           3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
#           4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}
#
# del people[3], people[4]
# print(people)

# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
#
# for i,j in people.items():
#     # print( i,j)
#     for key,value in j.items():
#         print(key,value)
#
# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
# if 1 in people:
#     for i,j in people[1].items():
#         print(i,j)


# myDict = {'ravi': 10, 'rajnish': 9,
#         'sanjeev': 15, 'yash': 2, 'suraj': 32}
# myKeys = list(myDict.keys())
# myKeys.sort()
# for i in myKeys:
#     myDict[i]=i
#     print(myDict)

#how to sort string

# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male',4:[2,3,5],'john_friend':{'name': 'Marie', 'age': '22', 'sex': 'Female,', 9:[1,2,4,5,6]}},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
#           }
# sum=0
# if 9 in people[1]['john_friend']:
#     for i in people[1]['john_friend'][9]:
#         sum=sum+i
# print(sum)

#sort dict by value
# dict1 = {'ravi': 10, 'rajnish': 9,'sanjeev': 15, 'yash': 2, 'suraj': 32}
# sorted_value=sorted(dict1.values())
#
# sorted_dict={}
# for i in sorted_value:
#     for j in dict1.keys():
#         if dict1[j] == i:
#             sorted_dict[j] = dict1[j]
#             break
# print(sorted_dict)

#sort by key
# dict1 = {'ravi': 10, 'rajnish': 9,'sanjeev': 15, 'yash': 2, 'suraj': 32}
# sorted_key=sorted(dict1.keys())
# sorted_dict1={}
# for i in sorted_key:
#     for j in dict1.values():
#         if dict1[i]==j:
#             sorted_dict1[i]=dict1[i]
# print(sorted_dict1)
# dict1 = {'ravi': 10, 'rajnish': 9,'sanjeev': 15, 'yash': 2, 'suraj': 32}
# for i in dict1:
#     print(dict1[i])

#update
# d = {"Name":"Ram" , "Age":23}#add {"City":"Salem"}
# d.update({"City":"Salem"})
# print(d)

# 3. Write a Python program to concatenate following dictionaries to create a new one.
# dict1 = {"Name" : "Ram" , "Age" : 23}
# dicty2 = {"City" : "Salem", "Gender" : "Male"}
# result=dict1.copy()
# result.update(dicty2)
# print(result)
#merge 3 dict
# dict1 = {"Name" : "Ram" , "Age" : 23}
# dict2 = {"City" : "Salem"}
# dict3 = {"Gender" : "Male"}
# dict4={}
# for i in (dict1,dict2,dict3) :
#     dict4.update(i)
# print(dict4)
#add 4 dict
# dict1 = {"Name" : "Ram" , "Age" : 23}
# dict2 = {"City" : "Salem"}
# dict3 = {"Gender" : "Male"}
# dict4 = {"Name" : "Ram" , "Age" : 23}#dont add because key and value are same
# dict5={}
# for i in (dict1,dict2,dict3,dict4):
#     dict5.update(i)
# print(dict5)
#
# dict1 = {"Name" : "Ram" , "Age" : 23}
# dict2 = {"City" : "Salem"}
# dict3 = {"Gender" : "Male"}
# dict4 = {"ame" : "Ram" , "A" : 23}
# for i in (dict1,dict2,dict3,dict4):
#     dict5.update(i)
# print(dict5)

 #Write a Python program to check whether a given key already exists in a dictionary.
# dict={'Name' : 'Ram', 'Age' : 23,}
# Key = 'Name'#check present or not
# print('Name' in dict)

# dict={'Name' : 'Ram', 'Age' : 23,}
# Key = 'Name'
# if 'Name' in dict:
#     print('true')
# else:
#     print('false')

''' Write a Python script to generate and print a dictionary that contains a number 
(between 1 and n) in the form (x, x*x).'''

# i=int(input('enter no'))
# dict={}
# for i  in range(1,i+1):
#     dict[i]=i**2
#     print(dict)

#remove None from value
# student = {"Name": "Pooja", "Age":23, "Gender": None, "Mark":488, "City": None}
# for key,value in student.items():
#     if value is  not None :
#         print(key,value)

# student = {"Name": "Pooja", "Age":23, "Gender": " ", "Mark":488, "City": " "}
# for key ,value in student.items():
#     if value is not  " ":
#         print(key,value)

# 17## Create a dictionary of keys a, b, and c
# Dictionary = { 'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#                           'Y' : [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
#                           'Z' : [21, 22, 23, 24, 25, 26, 27, 28, 29, 30] }
# A=[]
# if 'A' in Dictionary.keys():
#     for i in Dictionary['A']:
#         print(i)
#

#find same value in two dict
# a = {'Tamil': 92, 'English': 56, 'Maths': 88, 'Sceince': 97, 'Social': 89}
# b= {'Tamil': 78, 'English': 68, 'Maths': 88, 'Sceince': 97, 'Social': 56}
# for i,j in a.items():
#     for k,l in b.items():
#         if i==k and j==l:
#             print('present in both',i,j)

#find same key
# a = {'Tamil': 92, 'English': 56, 'Maths': 88, 'Sceince': 97, 'Social': 89}
# b= {'hindi': 78, 'histry': 68, 'Maths': 88, 'com sci': 97, 'Social': 56}
# for i,j in a.items():
#     for k,l in b.items():
#         if i==k:
#             print("same key in both dict",i)

# Write a Python program to count number of items in a dictionary value that is a list.
#
# dict =  {'M1': [67,79,90,73,36], 'M2': [89,67,84], 'M3': [82,57]}
# total=sum(map(len ,dict.values()))
# print("Number of Items in a Dictionary :",total)

# dict =  {'M1': [67,79,90,73,36], 'M2': [89,67,84], 'M3': [82,57]}
# print(len , dict.values())

#program to check multiple keys exists in a dictionary
# Dict = { 'name' : 'Ram', 'age' : 23, 'city' : 'Salem' }
# a={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# {'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}
# sorted_key=sorted(a.values())
# sorted_dict={}
# for i in sorted_key:
#     for j ,k in a.items():
#         if a[j]==i:
#             sorted_dict[j]=a[j]
# print(sorted_dict)

#sort by key
# dict1 = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# sorted_key=sorted(dict1.keys())
# sorted_dict1={}
# for i in sorted_key:
#     for j in dict1.values():
#         if dict1[i]==j:
#             sorted_dict1[i]=dict1[i]
# print(sorted_dict1)
# dict1 = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# new_sorted_dict={}
# for i  in sorted(dict1.keys()):
#     new_sorted_dict[i]=dict1[i]
# print(new_sorted_dict)

# def my_sorted(dict1):
#
#     sorted_key=sorted(dict1.keys())
#     sorted_dict1 = {}
#     for i in sorted_key:
#         for j in dict1.values():
#             if dict1[i] == j:
#                 sorted_dict1[i] = dict1[i]
#                 break
#     return sorted_dict1
# dict1 = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# print(my_sorted(dict1))

#Write a Python program to check multiple keys exists in a dictionary.
# dict = {
#   'name': 'Ram',
#   'age': 23,
#   'city': 'Salem'
# }
#
# Keys = {'age', 'name'}#to check
# print(dict.keys() >= {'age', 'name'})
# print(dict.keys() >= {'age', 'salary'})

# dict = {
#   'name': 'Ram',
#   'age': 23,
#   'city': 'Salem'
# }
# if 'name' in dict:
#     print('true')
# elif 'age' in dict:
#     print('true')
# else:
#     print('false')


# Write a Python program to print a dictionary line by line.
# Dict = {  "Sam" : {"M1" : 89, "M2" : 56, "M3" : 89},
#                "Suresh" : {"M1" : 49, "M2" : 96, "M3" : 89} }
# for i in Dict:
#     print(i)
#     for j in Dict[i]:
#         print(j,Dict[i][j])

#convrt two list in to dict
#also use zip method
# keys = ["One", "Two", "Three", "Four", "Five"]
# values = [1, 2, 3, 4, 5]
# res={}
# for i in keys:
#     for j in values:
#         res[i]=j
# print(res)

# Initialize dictionary with default values
# stu = ["Siva", "Sam", "Ram", "Pooja"]
# defaults = {"designation": "Student", "Department": "BCA"}
# result=dict.fromkeys(stu,defaults)
# print(result)

#print key value of given key
# student = {
#     "Name": "Tara",
#     "RollNo": 130046,
#     "Mark": 458,
#     "City": "Chennai"}
#
# keys = ["Name", "RollNo", "Mark"]
# for i in keys:
#     for j,k in student.items():
#         if i==j:
#             print(j,student[j])

#nested dict
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }
# for i in data:
#     print(data[i])

#Python program to get keys from the nested dictionary
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }
# for i  in data:
#     print(data[i].keys())

#Python program to get value  from the nested dictionary
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }
# for i in data:
#     print(data[i].values())

#print 5
# nested_lst=[[1,2,3], [4,5,6], [7,8,9]]
# #Type your answer here.
# print(nested_lst[1][1])
#
# # print 9
# print(nested_lst[2][2])
# #print 3
# print(nested_lst[0][2])

#print z
# nested_lst = [["Hat", "Glove", "Goggle"], ["Button", "Zipper", "Hook"]]
# print(nested_lst[1][1][0])

# What color is the violet?

# Print the values of the "roads" key from the nested dictionary.

# dict = {"Dakar":{"weathernested":"sunny", "roads":"dry"}}
# print(dict["Dakar"]['roads'])

# Print the first element of the weather for Tokyo.
# nested_dict = {"Tokyo": {"weather":["sunny", "cloudy"], "roads":"dry"}, "Dakar": {"weather":["foggy","windy"], "roads": "sandy"}}
# print(nested_dict['tokyo']["weather"][0])

# understand .format() method
# name=input('enter your name. ')
# str="hello !"
# print(str.format())

# str = "{}, {}, {}".format(1, 2, 3)
# print(str)

# str="One year has {} months, {} weeks and {} days.".format(12,54,365)
# print(str)

#use of indexing
# str = "One year has {2} months, {0} weeks and {1} days.".format(52, 365, 12)
# print(str)

# John=75
# Ann=80
# Ally=60
#
# str="Scores were as following: John:{}, Ann:{}, Ally:{}".format(75,80,60)
# print(str)

#join
# lst=["Hawaii", "Phuket", "Aruba", "Keys"]
# str='+++'.join(lst)
# print(str)

#correct email address
# addresses=("Mr.Hathaway", "amymail.com")
# e_mail="@".join(addresses)
# print(e_mail)

# join each element in the list with a space character: " "
# lst=['Everything', 'has', 'beauty,', 'but', 'not', 'everyone', 'can', 'see.']
# res=' '.join(lst)
# print(res)

#join dict key with ,
# data ={'Name': 'Bobby', 'Id': 1, "Age": 20}
# res=','.join(data)
# print(res)


# creating a nested dictionary named as student and here we are adding one more
# element in the dictionary
# student = {1: {'name': 'Shivam', 'age': '22', 'Id': 10053},
#           2: {'name': 'Anjali', 'age': '20', 'Id': 10004}}
# student[3]={}
# student[3]['name']='ram'
# student[3]['age']=22
# student[3]['Id']=102545
# print(student)
# print(student[3])

# for deleting particular elements from a particular dictionary indide the nested
# dictionary.
# student = {1: {'name': 'Shivam', 'age': '22', 'Id': 10053},
#           2: {'name': 'Anjali', 'age': '20', 'Id': 10004}}
# del student[1]['Id']
# print(student)


# student = {1: {'name': 'Shivam', 'age': '22', 'Id': 10053},
#           2: {'name': 'Anjali', 'age': '20', 'Id': 10004}}
# del student[1]
# print(student)

#today question 3/10/2023

#how to update element
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }
# data['Student 1']['Name']='python'#update
# print(data)

#how to add element
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }
# data['Student 1']['salary']=1200
# print(data)

# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }
# data['Student 4']={}
# data['Student 4']['name']='roshan'
# data['Student 4']['age']=22
# data['Student 4']['id']=4
#
# print(data)

#del element name from student 1
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }
# del data['Student 1']['Name']
# print(data)

#del dict 'Student 3'
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }
# del data['Student 3']
# print(data)


#4/10/2023

#add a key ti dict
# dict={'name': 'Shivam', 'age': '22', 'Id': 10053}
# dict['salary']=1200
# print(dict)

#concatenate three dict in to new one
# dict1={1:10,2:20}
# dict2={3:30,4:40}
# dict3={5:50,6:60}
# result={}
# for i in (dict1,dict2,dict3):
#     result.update(i)
# print(result)

#function for concatenate three dict in to new one
# dict1={1:10,2:20}
# dict2={3:30,4:40}
# dict3={5:50,6:60}
# def merge(dict1,dict2,dict3):
#     result={}
#     for i in (dict1,dict2,dict3):
#         result.update(i)
#     return result
# print(merge(dict1,dict2,dict3))



#merge two dict
# dict1={1:10,2:20}
# dict2={3:30,4:40}
# dict1.update(dict2)
# print(dict1)

#sum of all value
# dict={'name': 20, 'age': 33, 'Id': 10053}
# sum=0
# for i,j in dict.items():
#     sum=sum+j
# print(sum)

# dict1={'name': 20, 'age': 33, 'Id': 100}
# def sum_functin(dict1):
#     sum1=0
#     for i,j in dict1.items():
#          sum1=sum1+j
#     return sum1
# print(sum_functin(dict1))

#multiply aal items
# dict={'name': 2, 'age': 3, 'Id': 100}
# multiply=1
# for i,j in dict.items():
#     multiply=multiply*j
# print(multiply)
#function
# dict1={'name': 2, 'age': 3, 'Id': 100}
# def multiply(dict1):
#     multiple=1
#     for i,j in dict1.items():
#         multiple=multiple*j
#     return multiple
# print(multiply(dict1))




# list=[1,2,3,4]
# multiply=1
# for i in list:
#     multiply=i*multiply
# print(multiply)

#remove a key
# dict={'name': 2, 'age': 3, 'Id': 10053}
# del dict['name']
# dict.pop('name')
#
# print(dict)

#sort dict by key
# dict={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# sorted_dict= {}
# for i in sorted(dict.keys()):
#     sorted_dict[i]=dict[i]
# print(sorted_dict)

#find max min value
# dict={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# min=None
# max=0
# for i,j in dict.items():
#     if j>=max:
#         max=j
#     elif min is None or j<=min:
#         min=j
# print(max,min)

#find second smallest in list
# list=[1,5,4,2,36,5,8,7]
# small1=None
# small2=None
# for i in list:
#     if small1 is None or i<small1:
#         small2=small1
#         small1=i
#         print('small is ',small1)
#     elif small2 is None or i<small2:
#         small2=i
# print('second smallest no is ',small2)

# list=[1,5,4,2,36,5,8,7]
# list.reverse()
# print(list)

#random
# list=[1,5,4,2,36,5,8,7]
# random.choice(list)
# print(random.choice(list))


# remove duplicate from dict
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#                 }
# result={}
# for i,j in student_data.items():
#     if j not in result.values():
#         result[i]=j
# print(result)

#how to add element in each dict
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }

# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#                 }
# result={}
# for i,j in student_data.items():
#     if j not in result.values():
#         result[i]=j
# print(j)
# print(result)

#duplicate ,how many time duplicate comes
#

#add key vakue in every sub dict of nested dict
# nested_dict = {
#     'a': {'x': 1, 'y': 2},
#     'b': {'x': 3, 'y': 4},
#     'c': {'x': 5, 'y': 6}
# }
#
# # Key-value pair to add to each sub-dictionary
# new_pair = {'ram': 1}
#
# for key in nested_dict:
#     nested_dict[key].update(new_pair)
# print(nested_dict)


# nested_dict = {
#     'a': {'x': 1, 'y': 2},
#     'b': {'x': 3, 'y': 4},
#     'c': {'x': 5, 'y': 6}
# }
#
# # Key-value pair to add to each sub-dictionary
# new_pair = {'ram': 1}
# for i in nested_dict:
#     nested_dict[i]['ram']=2
# print(nested_dict)


# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#                 }
# result={}
# duplicate={}
# for i,j in student_data.items():
#     if j not in result.values():
#         result[i]=j
# print(result)



# print(duplicate)



# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#                 }

# duplicate={}
# for key, sub_dict in nested_dict.items():
#     for subkey, value in sub_dict.items():


#remove duplicate and print duplicate in another dict
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    }
# }

# result = {}
# duplicate = {}
#
# for key, value in student_data.items():
#     if value not in result.values():
#         result[key]=value
#     else:
#         duplicate[key]=value
# print(result,'\n',duplicate)


#create function for remove duplicate and print duplicate in another dict
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    }
# }
# def remove_dupli(student_data):
#     result = {}
#     duplicate = {}
#     for key,value  in student_data.items():
#         if value not in result.values():
#             result[key ]=value
#         else:
#             duplicate[key]=value
#     return result,duplicate
# print(remove_dupli(student_data))
#

# [5:11 PM, 10/6/2023] Arvind Khangarot: student_data = {
#     'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}
# }
#
# def remove_dupli(student_data):
#     result = {}
#     duplicate = {}
#     for key, value in student_data.items():
#         if value not in result.values():
#             result[key] = value
#         else:
#             duplicate[key] = value
#     return result
#     return duplicate
#
# # result_dict, duplicate_dict = remove_dupli(student_data)
#
# print("Result (No Duplicates):")
# print(result_dict)
#
# print("\nDuplicate Entries:")
# print(duplicate_dict)
from collections import Counter

# student_data = {
#     'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id4': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id5': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}
# }
# result = {}
# duplicate = {}
# duplicate_count = 0
#
# for key, value in student_data.items():
#     if value not in result.values():
#         result[key] = value
#     else:
#         duplicate[key] = value
#
#         for value1 in duplicate.values():
#             duplicate_count += 1
#
# print("Result (No Duplicates):")
# print(result)
#
# print("\nDuplicate Entries:")
# print(duplicate)
#
# print("\nDuplicate Count:")
# print(duplicate_count)

#
# student_data = {
#     'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id4': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id5': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}
# }
#
# # Create a dictionary to store value counts
# value_counts = {}
#
# # Iterate through the nested dictionaries and their values
# for data in student_data.values():
#     for value_list in data.values():
#         for value in value_list:
#             if value in value_counts:
#                 value_counts[value] += 1
#             else:
#                 value_counts[value] = 1
#
# # Iterate through the duplicate values and their counts
# for value, count in value_counts.items():
#     if count > 1:
#         print(f"Value: {value}, Occurrences: {count}")

#find duplicate value ??????????????????????????????????????????????????
# data = {
#     'A': 1,
#     'B': 2,
#     'C': 1,
#     'D': 3,
#     'E': 2,
#     'F': 1
# }
# value_counts = {}
#
# # Loop through the keys and values in the dictionary
# for key, value in data.items():
#     if value in value_counts:
#         value_counts[value] += 1
#     else:
#         value_counts[value] = 1
#
# # Display the duplicate values and their counts
# for value, count in value_counts.items():
#     if count > 1:
#         print(f"Value {value} occurs {count} times.")


# '''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of
# 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line.'''
#
# result=[]
# for i in range(2000,3200+1):
#     if i%7==0 and i%5 !=0:
#         result.append(i)
# print (','.join(result))



# Python program to find the factorial of a number provided by the user.
# change the value for a different result
# num = int(input('enter a no'))
# result =1
#
# if num < 0:
#     print('factorial not defined for negative num')
# else:
#     for i in range(1,num+1):
#         result=result*i
#     print(result)

# def factorial(n):
#
#     result=1
#     if n<0:
#         return 'factorial for 0 is not defined'
#     elif n==0:
#         return 1
#     else:
#         result=1
#         for i in range(1,n+1):
#             result=result*i
#         return result
# num=int(input('enter number'))
# result=factorial(num)
#
# print(f'factorila of {num} is {result}')
#
# x=int(input('enter num'))
# # factorial=1
# # for i in range(1,x+1):
# #     factorial=factorial*i
# # print(factorial)
# def factorial(num):
#
#     for i in range(1,num+1):
#         result = 1
#         result=result*i
#     return result
# num=int(input('enter num'))
# result=num
# print(factorial(num))



# print(result)
#
# print(f'factorila of {num} is {result}')

'''uestion: With a given integral number n, write a program to generate a dictionary 
that contains (i, i*i) such that is an integral number between 1 and n (both included).

Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''


# num= int(input('enter no'))
# for i in range(1, num + 1):
#     dict1[i]=i*i
# print(dict1)
#
# def dict2(num):
#     dict1 = {}
#     for i in range(1,num+1):
#         dict1[i]=i*i
#     return dict1
# num=int(input('enter no'))
# print(dict2)


##comma seprated
# input_user=input('enter  no')
# num_list=input_user.split(',')
# print(num_list)

# data = {
#     'A': 1,
#     'B': 2,
#     'C': 1,
#     'D': 3,
#     'E': 2,
#     'F': 1
# }
# remove_dupl={}
# dulicates={}
# value_counts={}
# for i,j in data.items():
#     if j not in remove_dupl.values():
#         remove_dupl[i]=j
#     else:
#         dulicates[i]=j
#         for value, count in value_counts.items():
#             if count > 1:
#                 print(f"Value {value} occurs {count} times.")
#
#
# print(remove_dupl)
# print(dulicates)

# data = {
#     'A': 1,
#     'B': 2,
#     'C': 1,
#     'D': 3,
#     'E': 2,
#     'F': 1
# }
# value_counts = {}
#
# # Loop through the keys and values in the dictionary
# for key, value in data.items():
#     if value in value_counts:
#         value_counts[value] += 1
#     else:
#         value_counts[value] = 1
#
# # Display the duplicate values and their counts
# for value, count in value_counts.items():
#     if count > 1:
#         print(value,count)


