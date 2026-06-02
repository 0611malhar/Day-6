# '''
# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
# '''
# class vector2d:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print("2D vector is:",self.x,"&",self.y)

# class vector3d(vector2d):
#     def __init__(self,x,y,z):
#         super().__init__(x,y)
#         self.z = z

#     def show(self):
#         print(f"3D vector is:{self.x},{self.y} and {self.z}")

# v2 = vector2d(2,3)
# v2.show()

# v3 = vector3d(2,3,4)
# v3.show()




# '''
# 2. Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog'.
# '''
# class animals:
#     def __init__(self,height,eating_habits):
#         self.height = height
#         self.eating_habits = eating_habits
    

# class pets(animals):
#     def __init__(self,height,eating_habits,pet_name):
#         super().__init__(height,eating_habits)
#         self.pet_name = pet_name

# class dog(pets):
#     def __init__(self,height,eating_habits,pet_name):
#         super().__init__(height,eating_habits,pet_name)

#     def bark(self):
#         print("Dog barks!!")

# d = dog(60,'Omnivore','Stuart')
# print(d.height)
# print(d.eating_habits)
# print(d.pet_name)




# '''
# 3. Create a class 'Employee' and add salary and increment properties to it. Write a method 'salaryAfterIncrement' method with a @property decorator with a setter which changes the value of increment based on the salary.
# '''
# class Employee:
#     def __init__(self, salary, increment):
#         self.salary = salary
#         self.increment = increment

#     @property
#     def salaryAfterIncrement(self):
#         return self.salary * self.increment

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, new_salary):
#         self.increment = new_salary / self.salary

# e = Employee(50000, 1.1)
# print(e.salaryAfterIncrement)
# e.salaryAfterIncrement = 60000
# print(e.increment)




# '''
# 4. Write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them.
# '''
# class complex:
#     def __init__(self,real,imag):
#         self.real = real
#         self.imag = imag

#     def __add__(self,other):
#         real_part = self.real + other.real
#         imag_part = self.imag + other.imag

#         result = complex(real_part,imag_part)
#         return result
    
#     def __mul__(self,other):
#         real_part = ((self.real*other.real)-(self.imag*other.imag))
#         imag_part = ((self.real*other.imag)+(other.real*self.imag))
        
#         result = complex(real_part,imag_part)
#         return result
        
#     def __str__(self):
#         return f"{self.real} + {self.imag}i"

# c1 = complex(2,3)
# c2 = complex(4,5)

# print(c1 + c2)
# print(c1 * c2)




# '''
# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
# '''
# class Vector:
#     def __init__(self, values):
#         self.values = values

#     def __add__(self, other):
#         result = []
#         for i in range(len(self.values)):
#             result.append(self.values[i] + other.values[i])
#         return Vector(result)

#     def __mul__(self, other):
#         dot = 0
#         for i in range(len(self.values)):
#             dot += self.values[i] * other.values[i]
#         return dot

#     def __str__(self):
#         return str(self.values)

# v1 = Vector([1, 2, 3])
# v2 = Vector([4, 5, 6])

# print(v1 + v2)
# print(v1 * v2)





# '''
# 6. Write_str_() method to print the vector as follows:
# 7i + 8j +10k
# Assume vector of dimension 3 for this problem.
# '''

# class vec:
#     def __init__(self,i,j,k):
#         self.i = i
#         self.j = j
#         self.k = k
        
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"

# c1 = vec(2,3,5)
# print(c1)




