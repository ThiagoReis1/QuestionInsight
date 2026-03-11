from numpy import*

numb = array(eval(input("Digite uma sequencia que voce deseja: ")))
vetor = zeros(size(numb), dtype = int)

for i in range(0, size(numb)):
	vetor[i] = numb[i] ** 2

print(vetor)