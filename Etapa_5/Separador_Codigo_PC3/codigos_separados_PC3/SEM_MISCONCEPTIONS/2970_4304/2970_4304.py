t=int(input("tempo de investimentos?"))
qf=1042000
qo=1500
import math
i= ((qf/qo)**1/t) - 1

if(i<=0.01):
	mensagem = "Real"
	
else:
	mensagem= "Irrea
	
print(round(i,5))
print(mensagem)