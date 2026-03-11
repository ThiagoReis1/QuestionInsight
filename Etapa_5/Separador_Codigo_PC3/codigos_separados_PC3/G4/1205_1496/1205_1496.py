from numpy import*
vet = array(eval(input("distancias dos saltos:")))
recorde = 8.95
a=0
b=0

while(a<size(vet)):
	if(vet[a]>recorde):
		b=b+1
	a=a+1
print(recorde)
print(b)