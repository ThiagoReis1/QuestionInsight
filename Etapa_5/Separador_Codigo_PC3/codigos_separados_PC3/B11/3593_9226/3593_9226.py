from numpy import*

vetor = array(eval(input("Digite o valor: ")))
total = 200
i = 0 
while i < size(vetor):
	if vetor[i] == 1:
		total = total / 2
	if vetor[i] == 2:
		total = total * 3
	if vetor[i] == 3:
		total = total / 2
	if vetor[i] == 4:
		total = total * 3
	if vetor[i] == 5:
		total = total / 2
	if vetor[i] == 6:
		total = total * 3
	i = i + 1

print(round(total,2))
