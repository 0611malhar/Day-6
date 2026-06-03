'''
1. Program to open three files (1.txt, 2.txt, and 3.txt). If any file is not present, print a message without exiting the program.
'''
files = ["1.txt", "2.txt", "3.txt"]

for file in files:
    try:
        f = open(file)
        print(f"{file} opened!")
        f.close()
    except FileNotFoundError:
        print(f"{file} not present!")



'''
2. Program to print the third, fifth, and seventh elements from a list using enumerate()
'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
for i,item in enumerate(my_list,start = 1):
    if i in (3,5,7):
        print(item)



'''
3. List comprehension to print a list containing the multiplication table of a user-entered number
'''
n = int(input("enter number"))
t = [n*i for i in range(1,11)]
print(t)



'''
4. Program to display a/b where a and b are integers. If b = 0, display Infinite by handling ZeroDivisionError.
'''
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Infinite")



'''
5. Store the multiplication table generated in Q3 in a file named Tables.txt
'''
num = int(input("Enter a number: "))
table = [num * i for i in range(1, 11)]
with open("Tables.txt", "w") as f:
    for value in table:
        f.write(str(value) + "\n")