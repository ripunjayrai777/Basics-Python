##23
# x = 5
# y = "hello"
# z = x + y
# print(z)



##use try–except block
##Taaki program crash na ho
##Aur hum custom message dikha saken

# x = 5
# y = "hello"
# try:
#     z = x + y                 #risky code
# except TypeError:
#     print("cannot add an int and a str")






##24 try-except working
# a = [1, 2, 3]

# try:
#     print("Second element = %d" % (a[1]))

#     # Throws error since there are only 3 elements in array
#     print("Fourth element = %d" % (a[3]))

# except:
#     print("An error occurred")





##25  
## try:
##     # risky code
## except IndexError:
##     # handle index error
## except ValueError:
##     # handle value error




##25 multiple except blocks
# def fun(a):
#     if a < 4:
#         # throws ZeroDivisionError for a = 3
#         b = a / (a - 3)
#     # throws NameError if a >= 4 because b is not defined in that case
#     print("Value of b = ", b)

# try:
#     fun(3)
#     fun(5)

# except ZeroDivisionError:
#     print("ZeroDivisionError Occurred and Handled")

# except NameError:
#     print("NameError Occurred and Handled")









##26 we can use else clause with try-except
## try: Jahan error aa sakta hai
## except: Agar error aaya to kya karna hai
## else: Sirf tab chalega jab--
## try block bilkul sahi se execute ho
## koi exception na aaye
## Agar error aaya → else skip ho jata hai



# def AbyB(a , b): 
# 	try: 
# 		c = ((a+b) / (a-b)) 
# 	except ZeroDivisionError: 
# 		print ("a/b result in 0 : zero division error") 
# 	else: 
# 		print (c) 
# # test above function 
# AbyB(6, 4) 
# AbyB(3, 3)



##try → problem ho sakti hai
##except → problem aayi to
##else → problem nahi aayi to





##27 finally clause
##try-kaam karna hai
##except- problem ayi to report karna hai
##finally- office band hone se pehle system ko off karna hai

# try: 
# 	k = 5/0  
# 	print(k) 
# except ZeroDivisionError: 
# 	print("Can't divide by zero") 

# finally: 
# 	print('This is always executed') 




##28Raising exceptions

