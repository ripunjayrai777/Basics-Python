#In Python, if 2 variable has the same value, then they refer the same memory space, otherwise different
a = 20
b = 30
print("Id of a= ", id(a)," b= " ,id(b))

if ( a is b ):
  print ("a and b have same identity")
  print("this is boy")
else:
  print ("a and b do not have same identity")







# if ( a is not b ):
#       print ("a and b do not have same identity")
# else:
#       print ("a and b have same identity")
