from numpy import*

vetor_de_inteiros = array(eval(input("Digite os valores: ")))
possibilidades = 0
n = zeros

for i in range(size(vetor_de_inteiros)):
	if vetor_de_inteiros[i] < 3:
		possibilidades = possibilidades + 1
		
print(possibilidades)
print(vetor_de_inteiros[i] < 3)