from numpy import*
vet=array(eval(input("pessoas: ")))
x='p,c,r,l,b'
x.split(',')
a=zeros(5,dtype=int)
cp=0
cc=0
cr=0
cl=0
cb=0
for x in range(size(vet)):
	if x=="p":
		cp+=1
	elif x=="c":
		cc+=1
	elif x=="r":
		cr+=1
	elif x=="l":
		cl+=1
	else:
		cb+=1
print(x)
	