# import random
# list1=[1,5,4,2,36,5,8,7]
# def a(list1):
#     ran=random.choice(list1)
#     return ran
# print(a(list1))

student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
                }
result={}
duplicate={}
for i,j in student_data.items():
    if j not in result.values():
        result[i]=j
print(result)


