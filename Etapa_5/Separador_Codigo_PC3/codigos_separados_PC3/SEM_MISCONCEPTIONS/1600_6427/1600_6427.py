from numpy import*

vetor_custo = array(eval(input("vetor_custo: ")))

i = 0
acumulador = 0
while(i < size(vetor_custo)):
	if(vetor_custo[i] > 80 ):
		acumulador += (vetor_custo[i]) * 0.15
		
	i += 1

total = sum(vetor_custo) - acumulador

print(round(total,2))
	
	
