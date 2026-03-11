altura_pessoal = float(input("digite a altura: "))
taxa_pessoal = float(input("didgite a taxa: "))

altura_chico = 1.5
taxa_chico = 0.02
anos = 0

while (altura_pessoal < altura_chico):
	altura_pessoal += taxa_pessoal
	altura_chico += taxa_chico
	anos = anos + 1
print(anos)
	