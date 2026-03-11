virus = float(input("Digite o num de virus: "))
leuc = float(input("Digite o num de leucocitos: "))
taxa_v = float(input("Digite o percentual por dia das copias: "))
taxa_l = float(input("Digite o percentual por dia dos leuc: "))

t = 1
while(2*leuc <= virus):
	virus = virus + virus * (taxa_v/100)
	leuc = leuc + leuc * (taxa_l/100)
	
	t = t + 1

print(t)