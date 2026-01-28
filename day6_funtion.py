##1. Basic function syntax

# def square(n):
#     '''funtion for square'''                       
#     print(n**2)


# print(square.__doc__)
# square(4)

# result = square(4)
# print(result)




# def square2(a):
#     return a**2

# result = square2(6)
# print(result)



#2 Funtion  with multiple parameters
##Write a function with takes parameters with multiple input and the return.

# def sum(a,b):
#     return a+b

# print(sum(4,6))



#3 Polymorphism in Functions
##Write a funtion  multiply that multiplies two numbers, but can also accept and multiply strings

# def multiply(p1, p2):
#     return p1* p2

# print(multiply(5,6))
# print(multiply('a', 6))
# print(multiply(6,'a'))





#4 Function returning multiple values
## create a function that return multiple values like- take radius as input and gives area and circumferen both as output

# def circle_stats(radius):
#     circum= 2*3.14* radius
#     area = 3.14 * (radius**2)
#     return circum, area

# print(circle_stats(6))

##handling----
# c, a = circle_stats(6)
# print("Circum : ", c)
# print("Area : ", a)




#5 Default Parameter value (Default Parameter)
##Write a funtion to greet user, if no name is provided greet by default name.

# def greet(name= "Ramesh"):
#     return "Hello "+ name + "!!" 

# print(greet("abhi"))
# print(greet())




#6 Lambda Functions (function in one line and for one time)
## Create a lambda function to compute the cube of a number. 

ramesh= lambda x: x**3
result = ramesh(6)
print(result)

# print(cube)
# print(cube(2))
# result = cube(3)
# print(result)








#7 Function with *args
# def my_function(*kids):
#     print("The youngest child is ", kids[2])
# my_function("Emil","Tobias","Linus")












#8 Recursion (function call in same def function)

# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1)

# print(fact(5))









# def greet():
#     """this is a greeting function"""
#     print("hello , good morning!")

# greet()

# print(greet.__doc__)




# def change(name, age=15):
#     print(name, age)

# change("abhay", 65)




# def my_function(*kids):
#     print("The youngest child is "+ kids[3])

# my_function("Emil","Tobias","Linus", "naptune" )
