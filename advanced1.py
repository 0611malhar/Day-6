# walrus := --> assign values to variable as part of expression
if (n:= len([1,2,3,4,5]))>3:
    print(f"{n} elements, <=3 expected")



# type definition
n : int = 5
name : str = "Ms"

def sum(a: int, b: int)->int:
    return a+b



# advanced type hints:
from typing import List, Union, Tuple, Dict

# list of int
no: List[int] = [1,2,3,4,5]

# tuple of str, int
person: Tuple[int,str] = (23,"Abcd")

# dict with str keys and int values
scores: Dict[str,int] = {"a" : 23,"b":19}

# union-> can hold multiple datatypes
ide: Union[int,str] = "id1245"
ide = 123



# match_case
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"

print(http_status(200))



# merge dictionary
d1 = {"a":1,"b":2,"c":3}
d2 = {"d":4,"b":2,"c":3}
m = d1|d2
print(m)



# multiple context manager
with(
    open("f1.txt") as f1,
    open("f2.txt") as f2
)



# exception handling
try:
    a = int(input("Enter a number"))
    print(a)

except Exception as e:
    print(e)
print("Thankyou")



# raise an error
a = int(input("Enter first num"))
b = int(input("Enter second num"))
if b==0:
    raise ZeroDivisionError("cannot divide num by 0")
else:
    print(f"The division a/b is {a/b}")



# try_else
try:
    a = int(input("Enter num:"))
    print(a)

except Exception as e:
    print(e)
else:
    print("i am inside else")



# finally
def main():
    try:
        a = int(input("Enter num:"))
        print(a)
        return

    except Exception as e:
        print(e)
        return
    finally:
        print("inside finally")
main()



# __name__ concept
# inside file module.py
def myFunc():
    print("Hello")
myFunc()
print(__name__)# ----> is file ko direct run kiya, to o/p -----> __main__
#inside file abc.py
from module import myFunc# ----> is file ko run kiya, to o/p -----> module

if name == "_main_":
    # If this code is directly executed by running the file its present in
    print("we are directly running this code")
    myFunc()
    print(_name_)



# global k/w-->changes values of global variable
a= 90
def f():
    global a
    a=9
    print(a)
f()
print(a)



#enumerate
l = [3, 513, 53, 535]
# index = 0
# for item in 1:
#     print(f"The item number at index {index} is {item}")
#     index += 1
# This can be simplified using enumerate function
for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")



# list comprehensions
myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

sq = [i*i for i in myList]

print(squaredList)