#print last char of string
# my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string[-1])

#print , from string
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string[7])

'''Given the code below, insert the correct negative index on line 3
in order to return the w character from the string.'''
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string[-10])

#retun in dex of b
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string.index("B"))

'''Given the code below, insert the correct method on line 3 in order to return the number of occurrences 
of the letter o in the string'''
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string.count('o'))

#covert all string to uppercase
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string.upper())

'''Given the code below, insert the correct method on line 3 in 
order to check of the string starts with the letter X.'''
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string.startswith('X'))

'''Given the code below, insert the correct method on line 3 in order to convert all uppercase letters to lowercase
and all lowercase letters to uppercase.'''
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string.swapcase())

'''Given the code below, insert the correct method on line 3 in order to remove all spaces (single Space characters from the keyboard) 
from the string.'''
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string.replace(" ",""))

'''Given the code below, insert the correct method on line 3 in order to replace
all the occurrences of letter i with the substring btc.'''
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string.replace('i','btc'))

'''Given the code below, insert the correct method on line 3 in order to split the entire string 
in two parts, using the comma as a delimiter.
'''
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string.split(","))


'''join the characters of the string using the & symbol as a delimiter.'''
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print("&".join(my_string))

'''insert the correct code on line 4 in order to concatenate my_string with the following string:'''

# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# my_other_string = "Poor guy!"
# print(my_string+my_other_string)

'''insert the correct method on line 3 in order to convert
the first letter of each word in the string to uppercase.'''

# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string.title())
#
# print(my_string.capitalize())#convert first char to capital
#
# print(my_string.isupper())#check all string is uppercase

'''use string formatting with the % operator on 
to map the values of 2010, 10k and Bitcoin to the corresponding formatting operators.'''

# my_string = "In %s, someone paid %s %s for two pizzas."
# print(my_string%("2010","10k","Bitcoin"))

'''use string formatting with the format() method on line 3 to
map the values of 2010, 10k and Bitcoin to the corresponding formatting operators.'''

# my_string = "In {}, someone paid {} {} for two pizzas."
# print(my_string.format("2010","10k","Bitcoin"))

'''use slicing and insert the correct code on line 3 in order
to return the substring 2010 from the string. Use positive indexes!'''

# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string[3:7])

#return output bitcoin using negative indexing
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string[-23:-16])

#return the first 12 characters in the string. Use a single, positive index!
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string[:12])

#last 9 characters of the string. Use a single, negative index!
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string[-9:])

#return the entire string in reversed order.
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string[::-1])

# my_string = "In2010someonepaid 10k Bitcoin for two pizzas."
# print(my_string[0:27:2])

#return every 7th character of the string, starting with the first character.
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# print(my_string[::7])

#print every 3re char of string
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string[::3])

# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string[10:])

#last 4 characters. Use a single, negative index!
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(my_string[-4:])


#Exercise 26 - Numbers & Booleans
#convert number to float
# num1 = 25
# num2=float(num1)
# print(type(num2))

#convert float to int
# num1 = 13.67
# num2=int(num1)
# print(type(num2))

# num1 = 25
# num2 = 8
# num3=num1%num2
# print(num3)
# print(num3==1)

# print(11//2)#round division

# num1 = -11
# num2 = abs(num1)
# print(num2 == 11) #should result in True

#n order to raise num1 to the power of num2.
# num1 = 10
# num2 = 5
# print(pow(num1,num2))

# remove the element of my_list located at index 5.
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# my_list.pop(5)
# print(my_list)

#add c++ at end of mylist
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# my_list.append('c++')
# print(my_list)
#remove element 30 from mylist
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# my_list.remove(30)
# print(my_list)

#return the index of the element 10.5 in my_list.
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
#
# print(my_list.index(10.5))

#insert the element 77 at index 4 in my_list.
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# my_list.insert(4,77)
# print(my_list)


#concatenate my_list with [100, 101, 102], by adding the latter at the end of my_list.
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
#
# my_list.extend([100, 101, 102])
# print(my_list)


#find out how many times does the element 20 occur in my_list.
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# print(my_list.count(20))

#sort list asending order
# my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
# my_list.sort()
# print(my_list)
# sorted_list=sorted(my_list)#dont change original list
# print(sorted_list)

#sort in reverse order


# my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
# reverse_list=sorted(my_list,reverse=True)
# print(reverse_list)

#min no
# my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
# print(min(my_list))


#create empty list
# my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
# my_list.clear()
# print(my_list)

#[30.01, 30.02, 30.03] to my_list and multiply the resulting list by 2.
# my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
# add=(my_list+[30.01, 30.02, 30.03])*2
# print(add)


# my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
# other_list=[2,55,8,9,8]
# print(my_list+other_list)

# return the element 20 from my_list based on its index.
# my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
# print(my_list.__getitem__(2))
# print(my_list[2])

#return the element Java from my_list based on its index (negative).
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# print(my_list[-2])

#return a slice made of [30, 'Python', 'Java'] from my_list based on positive indexes.
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# print(my_list[3:6])

#return a slice made of [30, 'Python', 'Java'] from my_list based on negative indexes.
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# print(my_list[-4:-1])

#return my_list except the first 3 elements, using a single, positive index.
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# print(my_list[3:])

#return my_list except the last 4 elements, using a single, negative index.
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# print(my_list[:-4])


#my_list except the first 3 elements, using a single, negative index.
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# print(my_list[-4:])

#return my_list except the last 2 elements, using a single, positive index.
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# print(my_list[:5])

#return every third element of my_list starting with the first element of the list.
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# print(my_list[::3])

#return every fourth element of my_list starting with the last element of the list.
# my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
# print(my_list[::-4])

#range
# my_range = range(10)
# print(list(my_range))

# my_range=range(0,10)
# print(list(my_range))


#use the correct argument(s) for the range() function on
# line 1 in order to return [10, 13, 16, 19] when converted to a list.
# my_range=range(10,20,3)
# print(list(my_range))


#range() function on line 1 in order to return [115, 120] when converted to a list.
# my_range=range(115,125,5)
# print(list(my_range))

# range() function on
# my_range=range(-75,-25,5)
# print(list(my_range))

# my_range = range(-25, 139, 30)
# print(list(my_range))  # [-25, 5, 35, 65, 95, 125]

# @return the value associated with key 4
# crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
# print(crypto[4])
# print(crypto.get(4))#method
#update the value associated with key 4 to "Cardano".
# crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
# crypto[4]="Cardano"
# print(crypto)
# add a new key-value pair to the dictionary: 6: "Monero"
# crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
# crypto[6]='Monero'
# print(crypto)
#return the number of key-value pairs in the dictionary.
# print(len(crypto))

#delete the key-value pair associated with key 3.
# Do not use a method as a solution for this exercise!
# crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
# del crypto[3]
# print(crypto)

# crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
# crypto.pop(3)
# print(crypto)
# crypto.__delitem__(4)
# print(crypto)

# $verify that 7 is not a key in the dictionary.
# crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
# print(7 not in crypto)

#get a list of tuples, where each tuple represents a key-value pair in the dictionary.
# crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
# result=crypto.items()
# print(list(result))


#sum of key
# crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
# print(sum(crypto))

#get a list of all the values in the dictionary.
# crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
# print(list(crypto.values()))

#get a list of all the keys in the dictionary.
# crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
# print(list(crypto.keys()))


#remove an arbitrary key-value pair from the dictionary.
# crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
# crypto.popitem()
# print(crypto)


#Data Type Conversions
#convert value to a string.
# value = 10
# conv=str(value)
# print(type(conv))

#convert value to an integer.
# value = 10
# conv=int(value)
# print(type(conv))

#value to float
# value = 10
# conv=float(value)
# print(type(conv))

#convert value to list
# value = "Hello!"
# print(list(value))

#convert value to bin value
# value = 10
# conv=bin(value)
# print(bin(value))
# print(type(conv))

#convert value to a hexadecimal representation.
# value = 10
# print(hex(value))

#convert value from binary to decimal notation.
# value = '0b1010'

# conv = int(value, 2)

# print(conv)

#convert value from hexadecimal to decimal notation.
# value = '0xa'
# print(int(value,16))

#prints out True! if x has 50 characters or more.
# x = "The days of Python 2 are almost over. Python 3 is the king now."
# if len(x)>=50:
#     print('true')

#prints out True! if x is a string and the first character in the string is T.
x = "The days of Python 2 are almost over. Python 3 is the king now."
# if x == 'str' or x.startswith('T'):
#     print('true')
# if type(x) is str or x.startswith('T'):
#     print('true')

'''True! if at least one of the following conditions occurs:

the string contains the character z
the string contains the character y at least twice'''

x = "The days of Python 2 are almost over. Python 3 is the king now."
# if 'Z' in x or x.count('y')>=2:
#     print('true')

'''True! if the index of the first occurrence of letter f
is less than 10 and prints out False! if the same condition is not satisfied.'''

# x = "The days of Python 2 are almost over. Python 3 is the king now"
# if x.index('f') < 10:
#     print('true')
# else:
#     print('false')


'''True! if the last 3 characters of the 
string are all digits and prints out False! otherwise.'''

# x = "The days of Python 2 are almost over. Python 3 is the king now"
# if x[-3:].isdigit():
#     print('true')
# else:
#     print('false')

'''True! if x has at least 8 elements and the element positioned at
index 6 is a floating-point number and prints out False! otherwise.'''
# x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]
# if len(x)>=8 and type(x[6]) is float:
#     print("true")
# else:
#     print('false')

'''True! if the second string of the first list in x ends with the letter h and the first string of the second list in x also ends with
the letter h, and prints out False! otherwise.'''

# x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]
# if x[3][1].endswith('h') and x[7][0].endswith('h'):
#     print('true')
# else:
#     print('false')

'''the third string of the first list in x ends with the letter h ,or
the second string of the second list in x also ends with the letter h'''
# x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]
# if x[3][2].endswith('h') or x[7][1].endswith('h'):
#     print('true')
# else:
#     print('false')

'''True! if the largest value among the first 3 elements of the list is less than or equal to the 
smallest value among the next 3 elements of the list. Otherwise, print out False!
Hint! Use the appropriate slices to make the comparison.'''

# x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]
# if max(x[0:3])<=min(x[3:6]):
#     print('true')
# else:
#     print('false')

'''True! if 115 appears at least once inside the list or if it is the first element in the list. 
Otherwise, print out False!'''
# x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]
# if x.count(115)>=1   or x[0]==115:
#     print('true')
# else:
#     print('false')

'''True! if the value associated with key number 5 is Perl or the number of key-value pairs
in the dictionary divided by 5 returns a remainder less than 2. Otherwise, print out False!
'''
# x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
# if x[5] == 'Perl' or len(x)%5<2:
#     print('true')
# else:
#     print('false')

'''True! if 3 is a key in the dictionary and the smallest value (alphabetically)
in the dictionary is C#.??????????????????????
'''
# x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
# print(sorted(x.values()))
# if 3 in x and sorted(x.values())[0]=='C#':
#     print('true')
# else:
#     print('false')
# print(sorted(x.values()))

'''True! if the last character of the largest (alphabetically) value in the dictionary is n. '''

# x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
# print(sorted(x.values()))#for check largest sorted value
# if sorted(x.values())[-1][-1]=='n':
#     print('true')
# else:
#     print('false')

'''True! if the largest key in the dictionary divided by the second largest key in the dictionary returns a remainder
equal to the smallest key in the dictionary'''

# x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
# if sorted(x.keys())[-1]%sorted(x.keys())[-2]==sorted(x.keys())[0]:
#     print('true')
# else:
#     print('false')

'''True! if the sum of all the keys in the dictionary is less than the number of characters
of the string obtained by concatenating the values associated with the first 5 keys in the dictionary
'''

# x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
#
# if sum(x)<len(x[1]+x[2]+x[3]+x[4]+x[5]):
#     print('true')
# else:
#     print('false')

'''True! if the 3rd element of the first range is less than 2, prints out False! if the 5th element
of the first range is 5, and prints out None! otherwise.'''

# x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
# if x[0][2]<2:
#     print('true')
# elif x[0][4]==5:
#     print('false')
# else:
#     print('None')

'''True! if the 3rd element of the 3rd range is less than 6, prints out 
False! if the 1st element of the second range is 5, and prints out None! otherwise.'''
# x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
# if x[2][2]<6:
#     print('true')
# elif x[1][0]==5:
#     print('false')
# else:
#     print('None')

'''True! if the last element of the first range is greater than 3, prints out False! if the last element
of the second range is less than 9, and prints out None! otherwise.'''

# x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
# if x[0][-1]>3:
#     print('true')
# elif x[1][-1]<9:
#     print('false')
# else:
#     print('None')


'''True! if the length of the first range is greater than or equal to 5, 
prints out False! if the length of the second range is 4, and prints out None! otherwise'''

# x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
# if len(x[0])>=5:
#     print('true')
# elif len(x[1])==4:
#     print('false')
# else:
#     print('None')

'''True! if the sum of all the elements of the first range is greater than the 
sum of all the elements of the third range, prints out False! if 
the largest element of the second range is greater than the largest element of the third range,
and prints out None! otherwise'''


# x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
# if sum(x[0])>sum(x[2]):
#     print('true')
# elif max(x[1])>max(x[2]):
#     print('false')
# else:
#     print('None')

'''True! if the largest element of the first range minus the second element of the 3rd range
is equal to the first element of the first range,
prints out False! if the length of the first range minus the 
length of the 2nd range is equal to the first element of the 3rd range,
prints out Maybe! if the sum of all the elements of the 3rd range
divided by 2 returns a remainder of 0,
and prints out None! otherwise.'''
# x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
# if max(x[0])-x[2][1]==x[0][0]:
#     print('true')
# elif len(x[0])-len(x[1])==x[2][0]:
#     print('false')
# elif sum(x[2])%2==0:
#     print('may be')
# else:
#     print('None')


'''True! if the sum of the last 3 elements of the first range plus the sum of the last 3 elements of the 3rd range is equal to the sum of the last 3 elements of the 2nd range, and prints out False! if the length of the first range times 2 is less than the sum of all the elements of the 3rd range.'''
# x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
# if sum(x[0][-3:])+sum(x[2][-3:])==sum(x[1][-3:]):
#     print('true')
# elif len(x[0])*2<sum(x[2]):
#     print('false')

'''true! if the 2nd character of the value at key 1 is also present 
in the value at key 4, and prints out False! otherwise.
'''

# x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
# if x[1][1] in x[4]:
#     print('true')
# else:
#     print('false')

'''True! if the second to last character of the value at key 3 is the first character of the value at key 5, 
and prints out False! otherwise.'''

# x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
# if x[3][1:]==x[5][0]:
#     print('true')
# else:
#     print('false')
# x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
#
# if x[3][-2] == x[5][0]:
#     print("True!")
# else:
#     print("False!")

'''true! if the number of characters of the smallest value 
in the dictionary is equal to the number of occurrences of letter a in the value at key 3, and prints out False! otherwise.'''
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
# if len(min(x.values()))==x[3].count('a'):
#     print('true')
# else:
#     print('false')
#print list in reverse
# x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
# for i in sorted(x,reverse=True) :
#     print(i)

#q-140 Write a for loop that iterates over the x list and prints out the index of each element.
# x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
# for i in x:
#     print(x.index(i))

'''iterate over the x list and multiply by 10 only the elements that are greater than 20 
and print them out to the screen.'''

# x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
# for i in x:
#     if i > 20:
#         print(i * 20)

'''multiply each element of x with each element of y, '''

# x = [2, 4, 6]
# y = [5, 10]
# for i in x:
#     for j in y:
#         print(i*j)

'''multiply each element of x with each element of y that is less than 12,'''

# x = [2, 4, 6, 8]
# y = [5, 10, 15, 20]
# for i in x:
#     for j in y:
#         if j<12:
#             print(i*j)

'''multiply each element of x that is greater than 5 with each element of y that is less than 12, '''
# x = [2, 4, 6, 8]
# y = [5, 10, 15, 20]
# for i in x:
#     if i > 5:
#         for j in y:
#             if j < 12:
#                 print(i*j)

'''multiply each element of x with each element of y that is less than or equal to 10, also printing the 
results to the screen. For y's elements that are greater than 10, multiply each element of x with y squared.'''
# x = [2, 4, 6, 8]
# y = [5, 10, 15, 20]
# for i in x:
#     for j in y:
#         if j<=10:
#             print(i*j)
#         else:
#             print(i*j**2)

'''print out each character in x doubled if that character is also inside y.'''

# x = "cryptocurrency"
# y = "blockchain"
# for i in x:
#     if i in y:
#         print(i*2)

'''for each element that is between 3 and 7 inclusively print out the result of multiplying that 
element by the second element in the same range.'''

# my_range = range(9)
# for i in my_range:
#     if 3 <= i <= 7:
#         print(i*my_range[1])

'''Write code that will iterate over the range starting at 1, up to but not including 11, with a step of 2, and for each element that is between 3 and 8 inclusively print out the result of multiplying that element by the last element in the same range. For any other element of the range (outside [3-8]) print Outside!'''
# for i in range(1,11,2):
#     if 3<= i<=8:
#         print(i*range(1,11,2)[-1])
#     else:
#         print('outside')

'''range starting at 5, up to but not including 25, with a step of 5, and for each element
that is between 10 and 21 inclusively print out the result of multiplying that element by the second 
to last element of the same range. For any other element of the range (outside [10-21]) print Outside
! Finally, after the entire range is exhausted print out The end!'''
# for i in range(5,25,5):
#     if 10 <=i<=21:
#         print(i*range(5,25,5)[-2])
#     else:
#         print("Outside!")
# else:
#     print('the end!')


try:
    print(25 % 5 ** 5 + 5)
except:
    print("Bug!")
else:
    print("Clean!")

