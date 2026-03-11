from numpy import*
x= array(eval(input("vetor: ")))
s=0
for i in range(0,size(x)):
	if(x[i]>x[0]+(x[0]*(50/100))):
		s=s+1
		print(i)
print(s)
