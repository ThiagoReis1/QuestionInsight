from numpy import*

c = array(eval(input()))

# variaveis loop

i = 0 # percorrer vetor custo
d = 0 # calcula o total de descontos

while (i < size(c)):
	
	if (c[i] > 80.0):
		
		d = d + 1
		
	
	i = i + 1

t = sum(c) - (d * 5)
print (t)