from numpy import*
nome=array(eval(input()))
v=array(eval(input()))
i = 0
d = 0
while(i<size(v)):
	if(nome[i]=='ARROZ'):
		d = d + 1.25*v[i]
	elif(nome[i]=='FEIJAO'):
		d = d + 2.6*v[i]
	elif(nome[i]=='BIS'):
		d= d + 1.80*v[i]
	elif(nome[i] == 'MIOJO'):
		d = d + 0.85*v[i]
	elif(nome[i]=='FANTA'):
		d = d + 3.20*v[i]
	i = i + 1
print(round(d,2))
