from numpy import*

nomes = array(eval(input("nome do alimento: ")))
quant = array(eval(input("quantidades: ")))

n= array(['BANANA', 'BIFE', 'FEIJOADA', 'OMELETE', 'TOMATE'])
q= array([0.97,2.95,1.27,1.04,0.2])

i=0
x=0
while (i< size(n)):
	if ((nomes[i]=='BANANA')):
		x= x + q[0]* quant[i]
		i=i+1
	elif ((nomes[i]=='BIFE')):
		x= x + q[1]* quant[i]
		i=i+1
	elif ((nomes[i]=='FEIJOADA')):	
		x= x + q[2]* quant[i]
		i=i+1
	elif ((nomes[i]=='OMELETE')):	
		x= x + q[]* quant[i]
		i=i+1