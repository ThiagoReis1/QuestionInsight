#Universidade Federal do Amazonas
#Nome:Dhiecon Pereira Marinho
#Nr de inscrição - 21352183

B = float(input("Qual a base maior do terreno?: "))
b = float(input("Qual a base menor do terreno?: "))
h = float(input("Qual a base menor do terreno?: "))
c = float(input("Qual o custo por m2: "))

custo_de_fertilizacao = (h*(B+b)/2)*c

print(round(custo_de_fertilizacao, 2))