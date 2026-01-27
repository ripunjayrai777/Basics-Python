#6 - eval() function evaluates the expression
# x= 'print(55)'
# eval(x)
# x= eval( '10+5' )
# print(x)	








#7
# x = format(0.5,'%')           	
# y = format(255,'X')            
# print(x)
# print(y)



# def add_num(a,b,) :
   
#      a+b

# print(add_num(3,5))      

# def AddOne(x,y) :
#     print(x+y)


# AddOne()


# def my_function(x):
   

# my_function(3)
# my_function(5)



# def sum1(a , b):    
#         r=a+b    
#         print("sum =",r)


# r=sum1(10,50)




# def min(a,b) :
#     if a<b :        
#         r=a    
#     else:       
#         r=b    
#     return(r)

# print(min(8,5))
# # max(9,3)

# f=120

# def  fact(n):   
#     f=1
#     i=1
#     while(i<=n):
#          f=f* i
#          i=i+1    
#     return(f)

# a=6

# print("fact=",fact(a))







def changeme( mylist ):   
    "This changes a passed list into this function"   
    mylist = [1,2,3,4] 
    # This would assi new reference in mylist  
    print ("Values inside the function: ", mylist)   
    return
# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)




