from numpy import*

v = array(eval(input("vetor: ")))

suma=0

for i in range(0,size(v)):
	if(v[i]==1):
		suma=suma+80
	elif(v[i]==2):
		suma=suma+40
	elif(v[i]==3):
		suma=suma+20
	else:
		break
print(suma)

