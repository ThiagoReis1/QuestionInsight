from numpy import*
v = array(eval(input("digite os andares que elv parou:")))
soma = 0
i = 1 
while(i<size(v)):
	if(v[i]>v[i-1]):
		x = (v[i]-v[i-1])
		soma = soma + x
	else:
		x = (v[i-1]-v[i])
		soma =  soma + x
	i = i + 1
print(soma)
	

			
			
			
			
			
		