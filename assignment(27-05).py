# Write a program that can find the smallest_deviser of a number example 35 has 5 and 15 has 3.
n = int(input("Enter num:"))
for i in range(2,n+1):
    if n%i==0:
        print(i,"is the smallest divisor")
        break

# Write a program that keep on taking input if I am typing +ve values and keep on adding them the moment I enter a -ve value the program stops and shows the sum of all +ve values entered.
add = 0
while True:
  n = int(input("Enter num:"))
  if n<0:
    print(add)
    break
  else:
    add+=n

# Write a function that takes a number as a parameter and returns True if it is divisible by any number other than 1 and itself.
n = int(input("Enter num:"))

def fact(n):
    for i in range(2,n):
        if n%i==0:
            return True
    return False
    
print(fact(n))
