from numpy import*
notas = array(eval(input("Digite o vetor nota: ")))
i = 0
med = 0

while(i < size(notas)):
	s = sum(notas) - min(notas)
	med = s / 2 
	i = i + 1
print(round(med, 2))
