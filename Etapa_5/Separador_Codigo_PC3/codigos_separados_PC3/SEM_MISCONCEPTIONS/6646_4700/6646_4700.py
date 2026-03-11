from numpy import*
vetor = array(eval(input("Vetor de notas: ")))
pesos = array([1,2,3])
i = 0
num = 0
den = sum(pesos)

while (i < size(vetor)):
	num  = num + vetor[i]*pesos[i]
	i = i+1
calc = num/den

print(round(calc,2))