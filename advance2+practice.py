# virtual env--> to use multiple versions of something by isolating it
# pip install virtualenv
# virtualenv env
# .\env\Scripts\activate.ps1
# deactivate

# pip freeze -> all installed packages list
# to write it all in a file:  pip freeze > requirements.txt
# pip install -r .\requirements.txt  --> to set up entire environment in a new sys



# lambda func __> func in form of an expression
# def sq(n):
#     return n*n

sq = lambda x: x*x
print(sq(5))



# join mthd
a = ['a','b','c','d','e','f','g','h']
b = "".join(a)
print(b)



from functools import reduce
# map
l = [1,2,3,4,5]
sq = lambda x: x*x
sqList = list(map(sq,l))
print(sqList)

# filter
def even(n):
    if n%2==0:
        return True
    return False
even_val = list(filter(even,l))
print(even_val)

# reduce
def add(a,b):
    return a+b
print(reduce(add,l))



'''
1. Write a program to input name, marks and phone number of a student and format it
using the format function like below:

"The name of the student is ms, her marks are 72 and phone number is 99999888"
'''
name = input("Enter name")
marks = input("Enter marks")
phn = input("Enter phn number")
print(f"The name of the student is {name}, her marks are {marks} and phone number is {phn}.")



'''
2. A list contains the multiplication table of 7. write a program to convert it to vertical
string of same numbers.
'''
l = [7,14,21,28,35,42,49,56,63,70]
st = []

s = lambda x: st.append(str(x))
list(map(s, l))
a = "\n".join(st)
print(a)



'''
3. Write a program to filter a list of numbers which are divisible by 5.
'''
def dev(n):
    if n%5 == 0:
        return True
    return False
x = [2,3,4,5,1,10,14,15]
even_val = list(filter(dev,a))
print(even_val)



'''
4. Write a program to find the maximum of the numbers in a list using the reduce
function.
'''
def mxm(a,b):
    if a>=b :
        return a
    return b
z = [2,3,4,5,1,10,14,15]
print(reduce(mxm,z))



'''
5. Run pip freeze for the system interpreter. Take the contents and create a similar
virtualenv.
'''
# pip freeze > requirements.txt
# virtualenv msenv
# .\msenv\Scripts\activate.psl
# pip install -r .\requirements.txt



'''
6. Explore the 'Flask' module and create a web server using Flask & Python.
'''
import flask from Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello,World!</p>"