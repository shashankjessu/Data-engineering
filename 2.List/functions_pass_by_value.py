def func(a:int,b:int):
    #local variable
    a=100
    b=200
    print(f"Id of a ={id(a)}. id of b = {id(b)}")

#int,str,float
a="anirudh"
b="qurana"
print(f"Id of a ={id(a)}. id of b = {id(b)}")
func(a,b)
print(a)
print(b)