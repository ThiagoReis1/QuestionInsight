altura_luna = 1.65
taxa_luna = 0.02

altura_x = float(input("Insira a altura: "))
taxa_cresc = float(input("Insira a taxa de crescimento: "))
ano = 0 

while (altura_luna >= altura_x):
	altura_luna = altura_luna + taxa_luna
	altura_x = altura_x + taxa_cresc
	ano += 1

print(ano)