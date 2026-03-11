altura_macaco = 1.4
taxa_macaco = 0.06

i = 0

alturaL = float(input("Altura leao: "))
taxa = float(input("Taxa de crescimento: "))

while(altura_macaco < alturaL):
	
	altura_macaco = altura_macaco * 1.06
	alturaL = alturaL * (1 + taxa)
	i = i + 1
print(i)
