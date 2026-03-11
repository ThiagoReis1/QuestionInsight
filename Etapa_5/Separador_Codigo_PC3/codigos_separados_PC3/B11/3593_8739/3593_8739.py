from numpy import*

vetor = array(eval(input("lancamentos: ")))

i = 0
p = 200

while i < size(vetor):
	if vetor[i] == 1:
		p = p / 2
	if vetor[i] == 2:
		p = p * 3
	if vetor[i] == 3:
		p = p / 2
	if vetor[i] == 4:
		p = p * 3
	if vetor[i] == 5:
		p = p / 2
	if vetor[i] == 6:
		p = p * 3
	i = i + 1
print(p)