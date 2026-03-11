from numpy import *
num = array(eval(input("NUmeros: ")))

for i in range(size(num)):
	if num[i]==9:
		num[i]=0
	else:	
	   num[i]=(num[i]+1)**3
		
print(num)		