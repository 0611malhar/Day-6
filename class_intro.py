### Basic class code:
# class emp:
#     name = "Ms"
#     lang = "Py"
#     hometown = "Jaipur"

#     def getInfo(self):
#         print("the lang is:",lang,".\nThe location is:",hometown,".")

# malhar = emp()
# malhar.age = 22  ### age-> obj/instance attribute,, name,lang,hometown -> class attribute 
# print(malhar.age,malhar.name, malhar.lang)
#  instance attribute has more priority than class attri. during assignment and retrival



### self parameter
# class emp:
#     name = "Ms"
#     lang = "Py"
#     hometown = "Jaipur"

#     def getInfo(self):## self used when methods are to be used
#         print("the lang is:"+self.lang+".\nThe location is:"+self.hometown+".")
# malhar = emp()
# emp.getInfo(malhar)



### static method-> no parameters, not even self
# class emp:
#     name = "Ms"
#     lang = "Py"
#     hometown = "Jaipur"

#     def getInfo(self):## self used when methods are to be used
#         print("the lang is:"+self.lang+".\nThe location is:"+self.hometown+".")

#     @staticmethod
#     def greet():
#         print("hi")

# malhar = emp()
# malhar.getInfo() # emp.getInfo(malhar) is same as this
# malhar.greet()



### constructor
# fuction which is automatically called with creation of obj
# class emp:
#     name = "Ms"
#     lang = "Py"
#     hometown = "Jaipur"

#     def __init__(self,name,lang,hometown):# dunder method which is automatically called(starts with __)
#         self.name = name
#         self.lang = lang
#         self.hometown = hometown
#         print("constructor")

#     def getInfo(self):## self used when methods are to be used
#         print("the lang is:"+self.lang+".\nThe location is:"+self.hometown+".")

#     @staticmethod
#     def greet():
#         print("hi")

# malhar = emp("AAbc","JSON","Delhi")
# malhar.getInfo()
# malhar.greet()
