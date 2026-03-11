# leia qtd de combustivel comum
qmc = float(input("Informe quantidade de combustivel comum: "))

# se combustivel comum menor que 17.5 mil litros
if qmc > 0.00 and qmc < 17.5:
	# adicao de coaxium e total misturado a combustivel comum
	tqcoaxium = qmc + 1.5
# se combustivel comum maior ou igual a 17.5 mil litros e menor que 35.0 mil litros
elif qmc >= 17.5 and qmc < 35.0:
	# adicao de coaxium e total misturado a combustivel comum
	tqcoaxium = qmc + 2.3
# se combustivel comum maior ou igual a 35.0 mil litros e menor que 50.0 mil litros
elif qmc >= 35.0 and qmc < 50.0:
	# adicao de coaxium e total misturado a combustivel comum
	tqcoaxium = qmc + 3.3
# se combustivel comum maior ou igual a 50.0 mil litros
elif qmc >= 50.0:
	# adicao de coaxium e total misturado a combustivel comum
	tqcoaxium = qmc + 4.7

# exibe total de combustivel comum com coaxium adicionado
print(round(tqcoaxium,1))