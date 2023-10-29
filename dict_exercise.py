# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

# Python - Access Dictionary Items
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])
#
# # Get the value of the "model" key:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["model"])

# There is also a method called get() that will give you the same result:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict.get("model"))

# Get Keys
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict.keys())
#Get Values

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict.values())

#Make a change in the original dictionary, and see that the values list gets updated as well:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
# print(thisdict.values())
# thisdict["brand"]="maruti"
# print(thisdict)
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict.items())

# Check if Key Exists
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#     print("yes,model' is one of the keys in the thisdict dictionary")

#Change Values
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["brand"]="maruti"
# print(thisdict)
#
# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"model":"maruti"})
# print(thisdict)

#add key and value using update
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"tyre":"mrf"})
# print(thisdict)


# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["tyre"]="mrf"
# print(thisdict)


#remove method
#remove item using pop method
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("brand")
# print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

#remove using del
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)


# The clear() method empties the dictionary:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)


# Print all key names in the dictionary, one by one:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#     print(x)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.keys():
#     print(x)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#     print(thisdict[x])
#You can also use the values() method to return values of a dictionary:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.values():
#     print(x)

#Loop through both keys and values, by using the items() method:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x,y in thisdict.items():
#     print(x,y)

#copy dict
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# dict1=thisdict.copy()
# print(dict1)

#Make a copy of a dictionary with the dict() function:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict=dict(thisdict)
# print(mydict)

#nested dict
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
# print(child)

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict1 = {
#     "company":"ford",
#
#     "color":["red",8,"ttt"]
# }
# thisdict11={
#     "compa":"ford",
#
#     "col":["red",8,"ttt"]
# }
# a={}
# for x in (thisdict,thisdict1,thisdict11):
#     print(x)
#     a.update(x)
# print(a)

#Access Items in Nested Dictionaries
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

# print(child["child3"]["name"])

#The fromkeys() method returns a dictionary with the specified keys and the specified value.
#Create a dictionary with 3 keys, all with the value 0:
# x=(1,2,5)
# y=(0)
# thisdict=dict.fromkeys(x,y)
# print(thisdict)
#
# x=(1,2,5)
# thisdict=dict.fromkeys(x)
# print(thisdict)

#nested dict acess
child = {
    "child1":{
        "name":"arv",
        "year":"2011"
    },
"child2":{
    "name":"aaa",
    "year":"2145"
},
"child3":{
    "name":"arvind",
    "year":"5858"
}
}
# print(child["child3"]["name"])#for acess data
# child["child3"]["name"]="ram"#for change value
# print(child["child3"]["name"])

# for del
# del child["child3"]["name"]
# print(child)

#del using popitem
# child.popitem()#del last key,value
# print(child)

#del using pop
child.pop(0)
print(child)
# print(child.get("child3"))#acess data using get
child.get()