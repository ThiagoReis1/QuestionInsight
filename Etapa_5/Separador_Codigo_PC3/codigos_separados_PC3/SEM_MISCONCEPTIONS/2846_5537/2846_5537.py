from numpy import*
vet = array(eval(input("Digite: ")))
saida = ones(size(vet), dtype=int)
a = 0
for i in vet:
	saida[a] = i*2
	a = a + 1
print(saida)