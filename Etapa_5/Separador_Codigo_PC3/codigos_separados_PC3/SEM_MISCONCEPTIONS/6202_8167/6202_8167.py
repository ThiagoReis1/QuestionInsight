altura_usuario = float(input("Informe a altura: "))
taxa_usuario = float(input("Informe a taxa de crescimento: "))

altura_bia = 1.69
taxa_bia = 0.01

anos = 0

while altura_usuario<=altura_bia:
	altura_bia = altura_bia + taxa_bia
	altura_usuario = altura_usuario+taxa_usuario
	anos = anos+1

print(anos)