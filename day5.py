#5
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7 ] 
# # print (list1[0])                                  
# # print ("list2[1:5]: ", list2[1:5])                            
# print ("list1[-3]: ", list1[-3])









#6

#Loop Through a List
# list1 = ['physics', 'chemistry', 1997, 2000]
# for x in list1:
#     print(x)



#Updating List
# list1 = ['physics', 'chemistry', 1997, 2000]
# list1[2] = 2001
# print ("New value available at index 2 : ", list1[2])
# print(list1)

# list1.append("Hindi")
# print(list1)
# list1.insert(0,'Maths')
# print("New updated list is :", list1)



# x =("apple","banana","cherry" )
# y =list(x)
# y[1] ="kiwi"

# x =tuple(y)
# print(x)
 


# t2 = ("apple" ,)
# print(type(t2))





#11
#Empty Tuple
# t1= ()
# print(type(t1)) 


# a tuple with one item
# t2 = ("apple" , )
# print(type(t2))


#NOT a tuple
# t3 = ("apple")
# print(type(t3)) 


#12 delete tuble
# a = (1, 2, 3 )
# del a 
# print( a )                                   




#15 set
# set1 = { 'physics', 'chemistry', 1997, 2000 }
# set2 = { 1, 2, 3, 4, 5, 6, 7  }
# print ("set1: ", set1)
# print ("set1[1]: ", set1[1] )            # Index not allowed in Set
# print ("tset2[3]: ", set2[-1] )          # Negative Index not allowed in set


# set1[0] = 100 # not allowed
# set3 = set1 + set2  # not allowed



#16
# s= { "apple","banana","cherry" }
# print(len(s))


#Check if Item in SET
# s= { "apple","banana","cherry"}
# if "apple" in s:
#       print("Yes, 'apple' is in the fruits SET")


#remove( ) 
# a = { 1, 2, 3, 'apple' }
# a.remove('apple')



# print(a)


#pop
# b= {5,1,2,3,'boy'}
# b.pop()    #  first it arrange in a order and then delete first element
# print(b)


#clear( )  and del 




#page 17

# DaysA = {"Mon", "Tue", "Wed" }
# DaysB = { "Wed", "Thu", "Fri", "Sat", "Sun" }
# D1 = DaysA | DaysB
# D2 = DaysA.union( DaysB  )
# print(D1)
# print(D2)





#26
# Adding new item in Dictionary
# dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict1['Height'] = 4
# print ( dict1 )

# dict1 = {'Name': 'Zara', 'Ages': 7, 'Class': 'First',  'xyz': 'Age'}
# if "Age" in dict1:
#        print("Yes, 'Age' is the key in the Dictionary")
# else :
#        print("Not matched")

# d= {'Name': 'Ajay', 'Age': 7, 'Class': 'First'}
# d['Age']= d['Age'] + 5
# print(d['Age'])



DaysA = {"Mon", "Tue", "Wed" }
DaysB = { "Wed", "Thu", "Fri", "Sat", "Sun" }
D1 = DaysA  DaysB 
print(D1)






#28
# dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict1.popitem()
# print(dict1)                


#29
# dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict2= dict1.copy( )
# print(dict2)
# dict3=dict(dict1)
# print(dict3)
