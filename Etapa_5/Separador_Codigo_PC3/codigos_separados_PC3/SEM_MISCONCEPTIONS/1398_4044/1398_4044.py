#---------------------------------------------------------------------
#  Universidade Federal do Amazonas
#  Instituto de Ciências Exatas
#  Departamento de Física
#
#  Micael Davi Lima de Oliveira - 21851626 - FB01 
#  
#  Questão 1: Esta questão tem como objetivo calcular o valor total
#             a ser pago para que toda uma área possa ser pulveriza-
#	           da. De tal forma, que haverá como dado de entrada o
#		        tempo de voo(minutos). A partir do valor inserido será 
#             calculado mediante algumas condições as despesas totais.
#			      
#---------------------------------------------------------------------

# Nesta parte do código, o usuário deverá inserir o respectivo tempo de 
# voo em minutos, tal que a variável que guardará o valor será do tipo
# inteiro(int).

tempo_voo = int(input("1. Por favor, informe o tempo de voo(em minutos) necessarios para a pulverizacao: "))

# Aqui entra a estrutura condicional, onde caso o tempo de voo fornecido
# seja inferior ou igual a 200 minutos,logo, o custo com as despesas de-
# verá ser menor. Será obedecido a seguinte expressão: (5000 + 100*tempo_voo)

# Por outro lado, caso a condição acima seja falsa, tem-se consequentemente
# um custo maior com as despesas. Dessa forma, será obedecido a seguinte 
# expressão: [8000 + (100*200) + (90*(tempo_voo - 200))]

if (tempo_voo <= 200):
	custo = 5000 + (100*tempo_voo)
else:
	custo = 8000 + (100 * 200) + (90 * (tempo_voo - 200)) 

# Por fim, será impresso o total das despesas considerando que o tempo
# de voo é maior e diferente de zero.
print(custo)