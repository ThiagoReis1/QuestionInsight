unidade = input("Digite M para m/s e K para Km/h para a unidade da velocidade: ").upper()
valor = float(input("Digite o valor da velocidade: "))
if unidade == "M":
	velocidade = 3.6*valor
else: 
	velocidade = valor/3.6
print(round(velocidade,2))