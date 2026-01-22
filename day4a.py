# example of while with continue--------------
#34
# count=0
# while (count < 10) : 
#         count = count + 1 
#         if count == 4 :
#             continue

#         print ( count, end=" " )




#Examples of for loop:---------------

#37
# for var in (1,2,3,4,5) :      
#     print ( 'The count is:', var )





# for var in "NIELIT Gorakhpur":
#     print(var, end="  ")





#38
# var=0
# for x in "Python Programming":
#     if x in ('a','e', 'i', 'o', 'u') :
#         var=var+1
#         print(x)

# print ('The numbers of vowels is :', var)









#40
# count=0
# for i in (1,2,3,4,5,6):
#       if i%2 ==0:
#           count=count+1
# else :
#      print ('The count is:', count)








#42
# count=0
# for i in [1 ,2 ,3, 4, 5,6]:
#     count=count+1
#     if count==3 :
#         break
#     print("Count : ", count)






#45
# count=0
# for i in [1 ,2 ,3, 4, 5]:
#     count=count+1
#     if count==3 :
#         continue
# print("Count :",count)








#47 (range)
# r=range( 1,  7)
# for x in r :
#    print( x)






#49






# r=range(1,11)   #(1,2,3,4,5,6,7,8,9,10)
# sum=0
# for i in r :
#     sum=sum + i
# print("sum ", sum)




#50
# count= 0
# for i in range(1,11):
#     if(i%2==0):
#         count+=1
#         print(i)
# print(count)










#enumerate function 
# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)        #enumerate(iterable, starts)

# print(list(x))





# 51

# Months = ["Jan", "Feb" , "Mar", "April", "May", "June"]
# x=enumerate(Months, 2)
# for  i in x:
#         print (i)



#example
# Months = ["Jan", "Feb" , "Mar", "April", "May", "June"]
# for i, m in enumerate(Months):
#     print(i,m)







#52
#Program to print odd numbers

# r=range(1,10,2)
# for i , m in enumerate(r):
#   print("Odd Number at index ", i, " is " , m)





#54
#the prime numbers from 2 to 100
# i = 2
# while(i < 100):
#       j = 2
#       while(j <= (i/2)):
#            if (i % j) ==0:
#                  break
#            j = j + 1
#       if(j > i/2):
#             print(i,  end="   ")
#       i = i + 1



#57
for i in range(1,6):
    for j in range(i) :
       print("*", end="  ")
    print()




