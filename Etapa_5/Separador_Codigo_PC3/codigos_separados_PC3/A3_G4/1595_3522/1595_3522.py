from numpy import*
notas = array(eval(input()))
soma = 0
c = 0
t = 0
while(c < size(notas)):
	if(notas[c]==min(notas)):
		notas[c] = 0
	else:
		soma = soma + notas[c]
	c = c + 1
print(round(soma/(size(notas)-1), 2))