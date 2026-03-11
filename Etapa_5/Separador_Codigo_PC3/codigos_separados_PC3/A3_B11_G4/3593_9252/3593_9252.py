from numpy import *
num = eval(input("Lances: "))
ptf=0
pti=200
i=0

while i<size(num):
	if num[i]==1:
		pti /= 2
	if num[i]==2:
		pti *=3
	if num[i]==3:
		pti /=2
	if num[i]==4:
		pti *=3
	if num[i]==5:
		pti /=2
	if num[i]==6:
		pti *=3
	i+=1
	
print(round(pti,2))	
	

