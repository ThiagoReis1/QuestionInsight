from numpy import*

notas = array(eval(input()))

i = 0

while(i < size(notas)):
	if(notas[i]<2):
		notas[i] = 0
	if(notas[i]>8):
		notas[i] = 10
		
	i = i + 1
	
print(notas)
		