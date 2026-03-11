from numpy import *

seq_acertos = array(eval(input("Informe a sequencia de acertos: ")))
pontos_alvo = [80, 40, 20, 10]

pontuacao_final = 0
i = 0
while (i < size(seq_acertos)):
	pontuacao_final += pontos_alvo[seq_acertos[i]-1]
	i += 1

print(pontuacao_final)