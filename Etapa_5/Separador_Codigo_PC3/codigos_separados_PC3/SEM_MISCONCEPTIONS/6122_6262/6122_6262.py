combustivel_comum = float(input("Digite a quantidade de combustivel"))
if combustivel_comum < 17.0:
	quantidade_coaxium = 0.8
elif combustivel_comum < 35.0:
	quantidade_coaxium = 1.3
elif combustivel_comum < 50.0:
	quantidade_coaxium = 2.1
else:
	quantidade_coaxium = 3.0

total_combustivel = combustivel_comum + quantidade_coaxium
print(round(total_combustivel,2))