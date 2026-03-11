# Talita Oliveira Gomes Passos
# Matricula - 21552161
# 14 de Julho de 2016
# Avaliacao 3 - Ex 1

idade = int(input("Digite a idade (0 a 130 anos): "))
peso = float(input("Digite o peso (0.0 a 550.0 kg): "))

print("Entradas:", idade, "anos", "e", peso, "kg")

if(idade <= 20 and peso <= 60):
	grupo_de_risco = "Grupo de risco: 9"
	print(grupo_de_risco)
elif(idade <= 20 and 60 < peso <= 90):
	grupo_de_risco = "Grupo de risco: 8"
	print(grupo_de_risco)
elif(idade <= 20 and peso > 90):
	grupo_de_risco = "Grupo de risco: 7"
	print(grupo_de_risco)
elif(20 < idade <= 50 and peso <= 60):
	grupo_de_risco = "Grupo de risco: 6"
	print(grupo_de_risco)
elif(20 < idade <= 50 and 60 < peso <= 90):
	grupo_de_risco = "Grupo de risco: 5"
	print(grupo_de_risco)
elif(20 < idade <= 50 and peso > 90):
	grupo_de_risco = "Grupo de risco: 4"
	print(grupo_de_risco)
elif(idade > 50 and peso <= 60):
	grupo_de_risco = "Grupo de risco: 3"
	print(grupo_de_risco)
elif(idade > 50 and 60 < peso <= 90):
	grupo_de_risco = "Grupo de risco: 2"
	print(grupo_de_risco)
elif(idade > 50 and peso > 90):
	grupo_de_risco = "Grupo de risco: 1"
	print(grupo_de_risco)
elif(idade < 0 or idade > 130 or peso < 0.0 or peso> 550.0):
	print("Dados invalidos")
