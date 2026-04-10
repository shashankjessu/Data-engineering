from copy import deepcopy
my_dict = {"name":"anirudh","age": 25 ,"gender":"male",
           "ages":[432,3,44,666,323]
           }

diction2 =deepcopy(my_dict)
my_dict["ages"][0]=1000

print(my_dict)
print(diction2)

print(id(my_dict))
print(id(diction2))