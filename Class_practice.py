# '''1. Create a Class "Programmer" for storing information of few programmers
# working at Microsoft.'''
# class Programmer:
#     company = 'microsoft'
#     skills = 'software engineer'
# p1 = Programmer()
# p1.skills = 'Devops'
# p1.name = 'jordan'
# print(p1.name,"\t",p1.skills ,"\t",p1.company)
# p2 = Programmer()
# p2.name = 'ms'
# print(p2.name,"\t",p2.skills ,"\t",p2.company)


# '''2. Write a class "calculator" capable of finding square, cube and square root of a
# number.'''
# class calc:
#     def __init__(self,num):
#         self.num = num
#     def calculation(self):
#         print("Square of number is:",num**2)
#         print("Cube of number is:",num**3)
#         print("Square root of number is:",num**0.5)

# num = int(input("Enter the number"))
# c = calc(num)
# c.calculation()


# '''
# 3. Create a class with a class attribute a; create an object from it and set 'a'
# directly using object.a = o. Does this change the class attribute?
# '''
# class Programmer:
#     a = 12
# p1 = Programmer()
# o = 23
# p1.a = o
# print(p1.a)


# '''
# 4. Add a static method in problem 2, to greet the user with hello.
# '''

# class calc:
#     def __init__(self,num):
#         self.num = num
#     @staticmethod
#     def greet():
#         print("hello")
#     def calculation(self):
#         print("Square of number is:",num**2)
#         print("Cube of number is:",num**3)
#         print("Square root of number is:",num**0.5)

# num = int(input("Enter the number"))
# c = calc(num)
# c.greet()
# c.calculation()



# '''
# 5. Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
# '''

# class train:
#     def __init__(self,dist):
#         self.dist = dist
#         self.total = 1000
#         self.occ = 450
#     def book_ticket(self):
#         if(self.total-self.occ>0):
#             print("Ticket booked")
#             self.occ+=1
#     def Get_Status(self):
#         if(self.total-self.occ>0):
#             print("Total seats available are:",self.total-self.occ)
#         else:
#             print("OOP's! we ran out of seats")
#     def Cost(self):
#         print("Total cost of your journey is:",2*self.dist)
        
# dist = int(input("Enter distance of your journey:"))
# c = train(dist)
# c.book_ticket()
# c.Get_Status()
# c.Cost()



# '''
# 6. Can you change the self-parameter inside a class to something else. Try changing self to "slf" and see the effects.
# '''

# class calc:
#     def __init__(slf,num):
#         slf.num = num
#     def calculation(slf):
#         print("Square of number is:",num**2)
#         print("Cube of number is:",num**3)
#         print("Square root of number is:",num**0.5)

# num = int(input("Enter the number"))
# c = calc(num)
# c.calculation()
