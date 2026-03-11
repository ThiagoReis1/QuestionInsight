'''
  TP 6: Repetição por contagem(for)
  
  |-----------|
  | Questão 1 |
  |-----------|

  Universidade Federal do Amazonas
  Instituto de Ciências Exatas
  Departamento de Física
  
  Micael Davi Lima de Oliveira - 21851626
  Turma: FB01  
'''
from numpy import* 
# importação de uma biblioteca não nativa no Python3, que é crucial para o trabalho com arrays.

# inicialmente, criou-se um vetor que irá armazenar a quantidade de alunos que estão matriculados
# em cada turma da escola. E sendo assim, esse vetor possui um tamanho definido pelo usuário, de
# tal forma que o separador de cada elemento é uma (vírgula).

# a função 'eval' do Python3 permite que o compilador interprete alguns caracteres pré-definidos,
# como por exemplo, uma vírgula; crucial para separar elementos. Além disso, em strings cada ele-
# mento precisa ser colocado entre aspas duplas, afim de que o computador possa 'compreender' o 
# tipo de dado inserido.
vec = array(eval(input("Quantidade de alunos matriculados em cada turma: ")))
cont = 0 # variável acumuladora

# um laço de repetição precisa ser repetido em uma quantidade equivalente ao tamanho do vetor inserido
# pelo usuário. Fora utilizado uma repetição por contagem, afim de que se possa percorrer todo o vetor
# quantidade à procura de quantidades que sejam pares. 

# pode-se afirmar que todo número par é necessariamente um número divisível por 2. Para cada vez que for
# achado um elemento par, será incrementado em uma unidade o valor da variável 'cont'. Essa variável
# tem a importante função de determinar o tamanho do vetor que armazenará os índices referentes às
# turmas, que possuem valores pares.
for i in range(size(vec)):
	if (vec[i] % 2 == 0):
		cont += 1

# será criado um outro vetor, cujo tamanho será igual a quantidade de elementos pares do vetor anterior.

# uma observação importante a ser destacada, é que deve estar expresso como um dos argumentos da
# função 'zeros', o tipo de elemento que o vetor irá armazenar. Quantidades de alunos é sempre um
# valor do tipo inteiro e positivo.
vec_par = zeros(cont, dtype = int)
j = 0 # variável contadora

# foi necessário construir um outro laço de repetição, pois apesar de o computador já ter uma variável
# que armazena a quantidade de turma pares, é necessário ainda saber qual o índice associados aos elemen-
# tos que possuem quantidade pares. 

# E por isso, o vetor digitado pelo usuário novamente será percorrido à procura de turmas pares. Contudo,
# desta vez, um outro vetor irá ter a função de armazenar esse índice.

# Uma observação crucial, é que foi necessário declarar uma nova variável contadora. Isto porque, além
# do 'i' que está presente no laço 'for', foi preciso construir uma variável 'j'. No entanto, 'j' apenas
# será incrementado nas vezes em que for encontrado uma turma par. Isto porque, o índice 'j' não coincide
# com o índice 'i', e portanto, seria uma grave equívoco não ter declarado uma segunda variável de controle.
for i in range(size(vec)): 
	if (vec[i] % 2 == 0):
		vec_par[j] = i
		j += 1

# Por fim, agora é apenas preciso imprimir, respectivamente: 
#	(1) O valor da variável 'cont', que acumulou a quantidade total de turmas que possuem quantidades pares.
#  (2) O vetor 'vec_par', que armazenou o valor de cada índice associado à turma com quantidade par.
print(cont)
print(vec_par)