from numpy import*

vt= array(eval(input("Informe a quantidade esperada: ")))
j=0
s=0

for i in range(size(vt)):
	if(vt[i]< vt[0]):
		j=i
		
		s=s+1

		print(j)	
#print(j)		
print(s)		