'''
  TP 6: Repetição por contagem(for)
  
  |-----------|
  | Questão 2 |
  |-----------|

  Universidade Federal do Amazonas
  Instituto de Ciências Exatas
  Departamento de Física
  
  Micael Davi Lima de Oliveira - 28151626
  Turma: FB01
'''

from numpy import*
# importou-se uma biblioteca para cálculos computacionais. Isto porque, será
# necessário utilizar funções específicas para o trabalho com arrays(matrizes). 

# O vetor 'vec_d' armazena os elementos organizados da mesma forma que o usuário inseriu. E portanto,
# os números inteiros deverão estar dispostos em ordem decrescente.
vec_d = array(eval(input("Vetor de numeros inteiros decrescentes: ")))
# O vetor 'vec_c' inicialmente será composto apenas por '0', mas numa quantidade equivalente ao 
# tamanho do vetor 'vec_d'. Isto porque, o vetor de saída é na verdade, apenas o vetor digitado lido
# de forma contrária, ou seja, do Último ---> Primeiro.
vec_c = zeros(size(vec_d), dtype = int)

# Um laço de repetição precisa ser criado para que o computador faça o vetor 'vec_c' de um índice [i], 
# receber exatamente o índice que está na outra extremidade, ou seja, [-1-i]. Isto porque, na computação
# por algum motivo, o '-1' simboliza o índice do último elemento, e conforme for decrementando o [-1], 
# estarei curiosamente percorrendo o vetor a partir do último elemento até o primeiro vetor.

# Uma observação importante é que seguindo a lógica mencionada acima, é possível encontrar uma equação
# matemática que represente o índice do primeiro elemento.
#   [-1 - i]        (1)
#   [-1 - (n - 1)]  (2)
#   [-1 + 1 - n]    (3)
#   [-n] = [0]      (4)

for i in range(size(vec_d)):
	# Criou-se uma restrição dentro do algoritmo. Isto porque, caso o usuário insira um vetor contendo 
	# apenas um único elemento, o compilador do Python3 indicou uma falha de sintaxe. Isto porque, seria
	# acessado um índice inexistente. E por isso, chegou-se à conclusão de que o Python3 não interpreta
	# um array de um só elemento como vetor, cujo elemento, seria vec[0], mas apenas como 'vec'.
	if (size(vec_d) > 1):
		vec_c[i] = vec_d[-1-i]
	else:
		vec_c = vec_d
# No fim, após o laço de repetição ter sido finalizado e sendo assim, todos os elementos do vetor saída
# receberam exatamente o vetor inicial lido de trás para frente, logo, é preciso apenas imprimir o vetor
# 'vec_c', cuja ordenação dos números é de forma crescente. Isto apenas será válido, se todos os elementos
# do vetor inicial foram necessariamente inseridos em ordem decrescente.
print(vec_c)	