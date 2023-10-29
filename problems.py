#Convert two lists into a dictionary
# name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
# roll_no = [4, 1, 3, 2]
# studata=dict(zip(name,roll_no))
# print(studata)

# Merge two Python dictionaries into one
# a={'Manjeet': 4, 'Nikhil': 1, 'Shambhavi': 3, 'Astha': 2}
# b={"raja":1,"Manjeet":8,"ask":88}
# c= {}
# for i in (a,b):
#     c.update(i)
# print(c)

# Print the value of key ‘history’ from the below dict
# child = {
#     "child1":{
#         "name":"arv",
#         "year":"2011"
#     },
# "child2":{
#     "name":"aaa",
#     "year":"2145"
# },
# "child3":{
#     "name":"www",
#     "year":"5858"
# }
# }
#
#
# print(child["child3"]["year"])
# sampleDict={'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}}
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# sampleDict["class"]["student"]["marks"]["history"]=90
# print(sampleDict["class"]["student"]["marks"]["history"])

# Delete a list of keys from a dictionary
# Keys to remove
# keys = ["name", "salary"]

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# sample_dict.pop("name")
# del sample_dict["name"]
# sample_dict.__delitem__("name")
# print(sample_dict)

# Check if a value exists in a dictionary
# cheked value = 200
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# # if 200 in sample_dict.values():
# if 200 in sample_dict.values():
#     print("yes")
# else:
#     print("no")

'''Rename key of a dictionary
city = location
salary stipend'''
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# sample_dict["location"],sample_dict["salary stipend"]=sample_dict.pop("city"),sample_dict.pop("salary")/done usimng update
#
# print(sample_dict)
# Convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# result=dict(zip(keys,values))
# print(result)

'''Change value of a key in a nested dictionary
emp3 salary= 8500'''
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict["emp3"]["salary"]=8500
# print(sample_dict)


# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(sample_dict.values())

#deleate two or three keys at a time.# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# # if 200 in sample_dict.values():
# if 200 in sample_dict.values():
#     print("yes")
# else: using i using for loop.also update it
'''Rename key of a dictionary
city = location
# salary stipend using update amd find min value of a dict'''
#multiple key delate
# a_dict = {'John': 32, 'Mel': 31, 'Nik': 33, 'Katie': 32, 'James': 29, 'Matt': 35}
# keys = ['Katie','Nik']
#
# for key in keys:
#     a_dict.pop(key)
# print(a_dict)
#check value is exist in dict
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# for i,j in sample_dict.items():
#     if j==30:
#         print("yes")
#         break
# else:
#     print("not present")
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# for i,j in sample_dict.items():
#     print(i,j)

# my_dict = {'nikhil': 1, 'manjeet': 10, 'Amit': 15}
# new_dict = {}
# for key, value in my_dict.items():
#     if key == 'Amit':
#         new_dict['Suraj'] = value
#     else:
#         new_dict[key] = value
# del my_dict
# my_dict = new_dict
# print(my_dict)

#merge two dict
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict3 = {**dict1, **dict2}
# print(dict3)

#method for rename keys
# a_dict = {'John': 32, 'Mel': 31, 'Nik': 33, 'Katie': 32, 'James': 29, 'Matt': 35}
# # a_dict['x']=a_dict.pop('John' )
# a_dict['x']=a_dict['John']
# del a_dict['John']
# print(a_dict)

#convert two list in dict
# a=[1,2,5,8,7,9]
# b=[1,5,4,7,8,54]
# # print(dict(zip(a,b)))
# for i in zip(a,b):
#     print(i)

#combine two dict
# a_dict = {'John': 32, 'Mel': 31, 'Nik': 33, 'Katie': 32, 'James': 29, 'Matt': 35}
# b_dict={'ram':1,'shyam':5}
# print({**a_dict,**b_dict})

'''Python program to print positive numbers in a list'''
# list1= [12, -7, 5, 64, -14]
# for i in list1:
#     if i > 0:
#         print(i)

'''Python program to print positive and negative numbers in a list'''
# list1= [12, -7, 5, 64, -14]
#
#
# for i in list1:
#     if i >0:
#         # print("positive no",i)
#         print(list1.count(i))
#     else:
#         print("no is neg", i)
#
#ermove duplicate using det method.output is unordered.
# list1= [12, -7, 5, 64, -14,12,5,64]
# list1=list(set(list1))
# print(list1)


#remove duplicate using from key.

# list1= [12, -7, 5, 64, -14,12,5,64]
# list1=list(dict.fromkeys(list1))
# print(list1)

#Python program to swap two elements in a list
# list1= [12, -7, 5, 64, -14,12,5,64]
# list1[0],list1[-1]=list1[-1],list1[0]
# print(list1)

#print positive and negative number
# list1= [12, 5, 64,5,66,85,7,4]
# sum1=0
# for i in list1:
#     sum1+=i
# print(sum1)
# countevenno=0
# countoddno=0
# for i in list1:
#     if i % 2==0:
#         # print(i)
#         countevenno+=1
#     if i%2!=0:
#         # print(i)
#         countoddno+=1
# print(f"even no is list is={[countoddno]}")
# print(f"od no in list is={[countoddno]}")


# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# message = f"my first bicycle was{bicycles[0]}"
# print(message)

# list1=[4,5,4,4,4,88,55]
# evenno=[]
# oddno=0
# for i in list1:
#     if i%2==0:
#       print(f"even no is ={[i]}")

#print even or odd no in list
# list1=[4,5,4,4,4,88,55]
# even_no=[]
# odd_no=[]
# for i in list1:
#     if i%2==0:
#         even_no.append(i)
#     if i%2!=0:
#         odd_no.append(i)
#
# print(even_no)
# print(odd_no)

list1=[4,5,4,4,4,88,55]
counteven_no=0
countodd_no=0
for i in list1:
    if i%2==0:
        counteven_no+=1
    if i%2!=0:
         countodd_no+=1
print(countodd_no)
print(counteven_no)



