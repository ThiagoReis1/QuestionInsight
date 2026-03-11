from numpy import *

custo = array(eval(input(" ")))

desc = 0 #custo com desconto
i = 0 #posicao
acum = 0
while i != size(custo):
	if custo[i] > 40:
		desc = desc + custo[i] - 2.5				
		acum = acum + 1
	i = i + 1

desconto = acum * 2.5
total = (sum(custo) - desconto)
	
print(total)
	 





