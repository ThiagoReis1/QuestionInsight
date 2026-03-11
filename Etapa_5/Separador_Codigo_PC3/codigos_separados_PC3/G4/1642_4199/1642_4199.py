from numpy import *

t =  array(eval(input("vetor com numero de alunos em cada turma: ")))

ncinco=0 #contador de cincos
j=0 #contador prara o vetor de turmas com cinco

for i in range (size(t)):			#percorrer todo tamanho
	if(t[i]%5==0):				#condicao
		ncinco = ncinco + 1 			#incrementacao

# vetor turmas com grupos divisiveis por 5
	
p = zeros(ncinco,dtype=int)
for i in range(size(t)):	#criacao do vetor resposta
	if(t[i]%5 == 0):		#repeticao
		p[j] = i 				#vetor criacao
		j = j + 1 	#vetor criacao

print(ncinco)
print(p)