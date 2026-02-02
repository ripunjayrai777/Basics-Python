# f=open('shukla.txt','w')
# str=input("Enter string")
# f.write(str)
# f.close()





#read from file
# f=open('text.txt','r')
# str=f.read()
# print(str)
# f.close()
# print()
# f=open('text.txt','r')



f=open('akash.txt','w')
print("enter text (end with @)")
while(str!='@'):
      str=input()
      if(str!='@'):
            f.write(str+"\n")
f.close()


f=open('akgjhkhsh.txt','r')
str=f.read()
print(str)
f.close()