from numpy import*

vet = array(eval(input()))
i = 0
pnt = 0

while(vet[i]<=3):
	if(vet[i]==1):
		pnt = pnt + 80
	elif(vet[i]==2):
		pnt = pnt + 40
	elif(vet[i]==3):
		pnt = pnt + 20
	i = i + 1
print(pnt)