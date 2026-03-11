from numpy import*
v = array(eval(input("insira os andares: ")))
i = 1
soma = 0
while(i<size(v)):
	if(v[i]>v[i-1]):
		x = (v[i] - v[i-1])*3
		soma =  soma + x
	else:
		x = (v[i - 1] - v[i])*3 
		soma = soma + x
	i = i+1
print(soma)	
	