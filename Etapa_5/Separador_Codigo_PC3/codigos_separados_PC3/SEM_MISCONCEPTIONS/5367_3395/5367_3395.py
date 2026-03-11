from numpy import*
cpf=array(eval(input("")))
i=0
total_soma=0
extra=[1,2,3,4,5,6,7,8,9]
while i< len(cpf):
	total_soma=total_soma+(cpf[i]*extra[i])
	i=i+1
	
print(total_soma%11
	  )