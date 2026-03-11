'''
	|-----------|
 	| Questão 2 |
 	|-----------|
	
	Universidade Federal do Amazonas
	Instituto de Ciências Exatas
	Departamento de Física
	
	Aluno: Micael Davi Lima de Oliveira
	Matrícula: 21851626 | Turma: FB01
'''

from numpy import* # é preciso importar a biblioteca numpy para utilizar a função array.

# o vetor 'vec' terá que armazenar todos os números reais positivos inseridos pelo usuário, onde
# para cada número digitado deve-se concatenar uma vírgula, para em seguida, digitar o próximo
# número. E por isso, utilizar-se a função eval para interpretar as vírgulas inseridas.
vec = array(eval(input("vetor de numeros reais positivos: ")))

i = 0 # variável contadora
media = 0 # variável acumuladora
while (i < size(vec)): # o vetor 'vec' será percorrido por um laço de repetição
	media += vec[i]**(1/2) # para cada número digitado deverá ser calculado a raiz quadrada 
	                       # e somar o resultado com o índice anterior, armazenando tudo numa
		                    # variável denominada media
	i += 1 # incrementa-se o 'i' para cada elemento calculado
media = (media/size(vec))**2 # a média quadrática é obtida pela razão da variável acumuladora(media)
                             # pela quantidade de elementos do vetor, que é obtida fazendo-se o uso
									  # da função 'size' cujo argumento é o vetor a ser descoberto a quantidade.
print("%.2f" %(media)) # no fim, é mostrado ao usuário a media quadrática dos elementos presentes no vetor,
                       # e com uma aproximação de 2 casas decimais.