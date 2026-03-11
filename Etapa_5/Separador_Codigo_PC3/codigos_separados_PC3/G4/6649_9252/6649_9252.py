from numpy import *
i=0
num = eval(input("Notas:"))
med = 0
peso = [3,2,4,1,3]
sump = sum(peso)
while i < size(num):
	med += num[i]*peso[i]
	i+=1
	
print(round(med/sump,2))	
	
	

