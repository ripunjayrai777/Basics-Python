a = 60                     #  60 = 0011 1100
b = 13                     # 13 = 0000 1101

c = a & b                # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)

c = a | b                 # 61 = 0011 1101
print ("Line 2 - Value of c is ", c)

c = a ^ b                 # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

c = ~a                     # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)
