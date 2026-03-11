from numpy import*
vet = array(eval(input("Tempo de chegada")))

i = min(vet)
x= 0
y=0

while(x < size(vet)):
	if(vet[x]==min(vet)):
		y= y +1
		print(x)
	x = x +1