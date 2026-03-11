virus = int(input("Qual o numero de copias do virus?"))
leuc = int(input("Qual o numero de leucocitos no sangue?"))
taxa_virus = float(input("Qual a taxa de multiplicacao do virus?"))
taxa_leuc = float(input("Qual a taxa de multiplicacao dos leucocitos?"))
taxa_virus = (taxa_virus/100 )
taxa_leuc = (taxa_leuc/100)
cresc_virus = virus * taxa_virus
cresc_leuc = leuc * taxa_leuc
t = 0
while( leuc < 2 * virus ):
	virus = virus + cresc_virus
	leuc = leuc + cresc_leuc
	cresc_virus = virus * taxa_virus
	cresc_leuc = leuc * taxa_leuc
	t = t + 1
print(t)
