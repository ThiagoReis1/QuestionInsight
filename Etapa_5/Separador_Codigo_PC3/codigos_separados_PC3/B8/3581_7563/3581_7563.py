from  numpy import*  

v = array(eval(input("")))

i = 0 
custo = 0 
desconto = 2.50 

while(i < size(v)):
	if  v[i] >= 40:
		desconto = v[i] - desconto 
		custo =custo+ v[i] - 2.50
	elif v[i] < 40:
		custo= custo+ v[i]
	i = i + 1

print(round(custo,2))
		
		