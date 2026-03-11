from numpy import*

notas=array(eval(input()))

i=0

while i< size(notas):
	if notas[i]>9 and notas[i]<=10:
		notas[i]=10
	if notas[i]>4 and notas[i]<5:
		notas [i]=4
	i=i+1
	
print(notas)