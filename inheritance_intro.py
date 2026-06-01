# class empp:
#     company = "ITC"
#     def show(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.salary}")

# class prog(empp):
#     company = "ITC Infotech"
#     def showLang(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.salary}")

# a= empp()
# b= prog()
# print(a.company,b.company)



# multiple inheritance

# class empp:
#     company = "ITC"
#     def show(self):
#         print(f"The name of the employee is {self.name} and the company is {self.company}")

# class coder:
#     language = "Python"
#     def printLang(self):
#         print("Language =",self.language)

# class prog(empp,coder):
#     company = "ITC Infotech"
#     def showLang(self):
#         print(f"The name of the employee is {self.name} and he is good with {self.language}")

# b= prog()
# b.name = 'ms'
# b.show()
# b.printLang()
# b.showLang()




# multi level
# class emp:
#     a=1
# class prog(emp):
#     b=2
# class manage(prog):
#     c=3

# o=emp()
# print(o.a)

# o=prog()
# print(o.a,o.b)

# o=manage()
# print(o.a,o.b,o.c)




# super keyword

# class emp:
#     def __init__(self):
#         print("employee constructor")
#     a=1
# class prog(emp):
#     def __init__(self):
#         print("prog constructor")
#     b=2
# class manage(prog):
#     def __init__(self):
#         super().__init__()# to call its parent class
#         print("manage constructor")
#     c=3

# # o=emp()
# # print(o.a)

# # o=prog()
# # print(o.a,o.b)

# o=manage()
# print(o.a,o.b,o.c)




# class method, method only for class, not obj, to make sure, instance attri does not overwrites class attri.
# class emp:
#     a=1
#     @classmethod# without this, o/p -> 45,, self ki jagah cls use karega
#     def show(cls):
#         print("The class attribute of a is:",cls.a)

# e = emp()
# e.a = 45
# e.show()




