'''
---------------------------------------------------
	|-----------|
	| Questão 2 |
	|-----------|
	
	Universidade Federal do Amazonas
	Instituto de Ciências Exatas
	Departamento de Física
	
	Micael Davi Lima de Oliveira - 21851626 - FB01
	
	TP4 - Repetição por Condição(while)	
----------------------------------------------------
'''
# inicializa-se a variável 'result' por um valor neutro, que não
# interfira nem na pontuação, nem no laço while.
result = "" 

v = 0
e = 0
d = 0

while (result.upper() != "X"): # o laço é finalizado quando é digitado 'x'.
	result = input("(V)Vitoria - (E)Empate - (D)Derrota \n * Resultado: ")
	
	if (result.upper() == "V"):
		v += 3
	elif (result.upper() == "E"):
		e += 2
	elif (result.upper() == "D"):
		d += 1
		
print("%d" %v) # é impresso o total de pontos obtidos com vitórias.
print("%d" %e) # é impresso o total de pontos obtidos com empates.
print("%d" %d) # é impresso o total de pontos obtidos com derrotas.