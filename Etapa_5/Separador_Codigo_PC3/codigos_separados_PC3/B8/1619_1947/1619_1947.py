from numpy import*
vetor1=array(eval(input("Tempo de banho:")))
vetor2=array(eval(input("Tipos de banho").upper()))
total=zeros(size(vetor1), dtype = float)
i = 0
h = 0
while i < size(total):
	if vetor2[i] == 'QUENTE':		
		total[h] = 90 * vetor1[i] * 0.005
		h = h + 1
	elif vetor2[i] == 'MORNO':
		total[h] = 45 * vetor1[i] * 0.005
		h = h + 1
	elif vetor2[i] == 'FRIO':
		total[h] = 0 * vetor1[i] * 0.005
		h = h + 1

	i = i + 1
print(round(sum(total), 2))