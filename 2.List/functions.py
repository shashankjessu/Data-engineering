from typing import List

def func(lst:List[int]):
    print(f"inside func = {lst}")
    print(f"Id of lst = {id(lst)}")
    lst.append(100)
    print(f"After appending inside func = {lst}")

list1=[321,543,65675,7657,65]
print(f"Id of list1 = {id(list1)}")
func(list1)
print(f"outside func ={list1}")