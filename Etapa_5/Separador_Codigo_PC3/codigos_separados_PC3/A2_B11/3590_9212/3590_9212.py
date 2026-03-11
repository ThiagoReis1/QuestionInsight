from numpy import*

vetor = array(eval(input("digite o numero jogado:")))
pt = 0
i = 0

while i < size(vetor):
	if vetor[i] == 1:
		pt += 10
	if vetor[i] == 2:
		pt += 5
	if vetor[i] == 3:
		pt = pt
	if vetor[i] == 4:
		pt += 5
	if vetor[i] == 5:
		pt += 20
	if vetor[i] == 6:
		pt += 10
	i += 1
print(pt)
