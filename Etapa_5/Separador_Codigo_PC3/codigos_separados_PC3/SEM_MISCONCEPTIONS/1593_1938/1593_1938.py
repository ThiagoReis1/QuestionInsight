from numpy import*
notas = array(eval(input("")))

i = 0
j = 1
k = 0
total = 0

while(i < size(notas)):
	k = k + j
	total = total + notas[i] * j 
	i = i + 1
	j = j + 1	
	
print(round(total/k,2))