from numpy import*

vetor_tempo = array(eval(input("Digite um vetor: ")), dtype = int)
vetor_percentual = array(eval(input("Digite um vetor: ")), dtype = int)
i = 0

while(size(vetor_tempo) == size(vetor_percentual)):
	vetor_percentual[i] = vetor_percentual[i]*0.05*vetor_tempo
	vetor_novo = vetor_percentual

print(sum(vetor_novo))