'''
-------------------------------------------------
	|-----------|
	| Questão 1 |
	|-----------|
	
	Universidade Federal do Amazonas
	Instituto de Ciências Exatas
	Departamento de Física
	
	Micael Davi Lima de Oliveira - 21851626 - FB01
	
	TP4 - Repetição por Condição(while)
--------------------------------------------------
'''
# será digitado um número 'x', no qual a série geométrica
# estará em função.
x = float(input("Numero real x: "))

# a variável 'k' representa a precisão do resultado obtido,
# e sendo assim, a quantidade de termos que deverão ser cal-
# culados, limitando a quantidade de repetições do while.
k = int(input("Quantidade de termos na serie geometrica de MacLaurin: "))

i = 0 # variável contadora
soma = 0 # variável acumuladora

if ((x > -1) and (x < 1)) and (k > 0): # restrições do algoritmo
	while (i < k): # o laço deverá repetir k vezes
		soma += (x**i)*((-1)**(i))  # regra geral da série
		i += 1 # para cada repetição, a variável contadora é incrementada
	print("%.7f" %soma) # é mostrado o somatório com 7 casas de arrendondamento
else:
	print("Dados de entrada invalidos.")
