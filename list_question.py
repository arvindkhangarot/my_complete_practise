# How to iterate over 2+ lists at the same time
# name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
# animal = ['Cat', 'Dog', 'Fish', 'Goat']
# age = [1, 2, 2, 6]
# z = zip(name, animal, age)
# z #=> <zip at 0x111081e48>
# for name,animal,age in z:
#     print("%s the %s is %s" % (name, animal, age))

#reverse list
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1[::-1])#using negative index
# print(list1)

#Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# for x,y in zip(list1,list2):
#     print(x,y)
#
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3=[i+j for i,j in zip(list1,list2)]
# print(list3)

'''Turn every item of a list into its square'''
# numbers = [1, 2, 3, 4, 5, 6, 7]
# a=[]
# for i in numbers:
#     b=i**2
#     a.append(b)
#
# print(a)


#Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# result=list(filter(None,list1))# N in None is always capital
# print(result)

#Add new item to list after a specified item
#Write a program to add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# # list1[2]=[300, 400, [5000, 6000], 500]
# # list1[2][2]=[5000, 6000]
# # ist1[2][2]
# list1[2][2].append(7000)
# print(list1)

#Extend nested list by adding the sublist
#You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"]
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
# sub_list = ["h", "i", "j"]
# list1[2]="c", ["d", "e", ["f", "g"], "k"], "l"]
# list1[2][1]=["d", "e", ["f", "g"], "k"]
# list1[2][1][2]=["f", "g"]
# list1[2][1][2].extend(sub_list)
# print(list1)


#zip function
# Use the zip() function. This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it.
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# # print(list(zip(list1,list2)))
# for i ,j in zip(list1,list2):
#     print(i,j)

# Exercise 3: Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]
# squre=[]
# for i in numbers:
#     i=i**2
#     squre.append(i)
# print(squre)

# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# for x in list1:
#     for y in list2:
#         print(x,y)

# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# res=list(filter(None,list1))
# print(res)

# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)


# Exercise 8: Extend nested list by adding the sublist
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# # sub list to add
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(["h", "i", "j"])
# print(list1)
# Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
# list1 = [5, 10, 15, 20, 25, 50, 20]
# print(list1.index(20))
# if 20 in list1:
#     list1[3]=200
#     print(list1)
#

'''Exercise 10: Remove all occurrences of a specific item from a list.
Given a Python list, write a program to remove all occurrences of item 20.'''
# list1 = [5, 20, 15, 20, 25, 50, 20]
# n=20
# for x in list1:
#     if x==n:
#         list1.remove(x)
# print(list1)
#swap
# Input =[12, 35, 9, 56, 24]
# Input[0],Input[-1]=Input[-1],Input[0]
# print(Input)


'''Syntax	Description
print (list)	To print complete list
print (list[i])	To print ith element of list
print (list[i], list[j])	To print ith and jth elements
print (list[i:j])	To print elements from ith index to jth index
print (list[i:])	To print all elements from ith index
print (list * 2)	To print list two times
print (list1 + list2)	To print concatenated list1 & list2'''
# list =[12, 35, 9, 56, 24]
# print (list[0],list[2])
# print(list[0:3])
# print(list[0:])
# print(list[:3])
# print(list*2)

#Remove first occurrence of a given element
# list =[12, 35, 9, 56, 24,12]
# list.remove(12)
# print(list)

#Python | Remove all occurrences a given element from the list
# list =[12, 35, 9, 56, 24,12]
# n=12
# for i in list:
#     if i==n:
#         list.remove(n)
# print(list)

#Remove all elements in a range from the Python list
# list1 = [10, 20, 30, 40, 50]
# del list1[0:]
# print(list1)

# list1 = [10, 20, 30, 40, 50]
# del list1[0:2]
# print(list1)


#add
# list1 = [10, 20, 30, 40, 50]
# list1[3]=77
# list1.append(1)
# list1.insert(4,11)
# print(list1)

#Sort a list in ascending order
# list1 = [99,95,4,10, 20, 30, 40, 50]
# list1.sort()
# print(list1)



#sort in decending order
# list1 = [99,95,4,10, 20, 30, 40, 50]
# list1.sort(reverse=True)
# print(list1)

#find the differences i.e., the elements which do not exist in the second list.
# list1 = [10, 20, 30, 40, 50]
# list2 = [10, 20, 30, 60, 70]

# printing lists
# print("list1:", list1)
# print("list2:", list2)

# finding and printing differences
# of the lists
# print("Difference elements:")
# print(list(set(list1) - set(list2)))

#Difference between two lists
# li1 = [10, 15, 20, 25, 30, 35, 40]
# li2 = [25, 40, 35]
#
# temp3 = []
# for i in li1:
#     if i  not in li2:
#         temp3.append(i)
# print(temp3)

#find comman number in two list
# li1 = [10, 15, 20, 25, 30, 35, 40]
# li2 = [25, 40, 35]
# a=[]
# for i in li1:
#     if i in li2:
#         a.append(i)
# print(a)

#find the position of minimum and maximum elements of a Python list?
# list=[88,2,1]
# min = list.index (min(list))
# max = list.index (max(list))
# print(min)
# print(max)

# list=[88,2,1]
# min=list[0]
# max=list[0]
# a=[]
# b=[]
# for i in list:
#     if i>max:
#         max=i
#         a.append(i)
#     elif i <min:
#         min=i
#     b.append(i)
#
#
#
#
# print(a)
# print(b)

#Given a list and we have to find the index of first matched of a list
# list1 = [10, 20, 10, 20, 30, 40,"", 50]
#
# print(list(filter(None,list1)))
# # esult=list(filter(None,list1)

#remove duplicate
#et suppose, 20 is available three times in the list list1 and when we append 20 (first occurrence) to the list list2, it will be appended, but when we append 20 (second occurrence) to the list list2, condition will be false and item will not be appended. And finally, we will get list without duplicate elements.
# ist1 = [10, 20, 10, 20, 30, 40, 30, 50]
# # list1=[]
# # for i in ist1:
# #     if i not in list1:
# #         list1.append(i)
# # print(list1)

# list1=[10, 20, 10, 20, 30, 40, 30, 50]
# print(list(set(list1)))

# list1=[10, 20, 10, 20, 30, 40, 30, 50]
# print(list(dict.fromkeys(list1)))

#even amd odd number
# List1 = [11, 22, 33, 44, 55]
# even=[]
# odd=[]
# for i in List1:
#     if i%2==0:
#         even.append(i)
#
#     elif i%2 !=0:
#         odd.append(i)
#
# print("even no is",even)
# print("odd no is ",odd)

# print the numbers which are divisible by M, N
# List1 = [10, 15, 20, 25, 30]
# M = 3
# N=5
# for i in List1:
#     if i%M==0 and i%N==0:
#         print(i)


#create a list from the specified index of the list.
# list = [10, 20, 30, 40, 50, 60]
# start = 1
# end = 4
# Example 1
# list = [10, 20, 30, 40, 50, 60]
# start = 1
# end = 4
# # list1: [20, 30, 40, 50]
#
# list1=list[start:end+1]
# print(list1)


# list : [10, 20, 30, 40, 50, 60]
# start = 1
# end   = 6
# list1=list[start:end+1]
# print(list1)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# for i in players[0:3]:
#     print(i)

#2. How to iterate over 2+ lists at the same time
# name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
# animal = ['Cat', 'Dog', 'Fish', 'Goat']
# age = [1, 2, 2, 6]
# for x,y,z in zip(name,animal,age):
#     print(x,y,z)
