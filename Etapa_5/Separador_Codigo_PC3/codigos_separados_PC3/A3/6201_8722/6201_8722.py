altura_joe = 1.77
taxa_joe = 0.02

altura_randola = float(input("Qual a altura do randola? "))
taxa_randola= float(input("Qual a taxa de crescimento do randola? "))
cont = 0

while altura_randola < altura_joe:
	altura_joe = altura_joe + 0.02
	altura_randola = altura_randola + taxa_randola
	cont = cont + 1
	
print(cont)