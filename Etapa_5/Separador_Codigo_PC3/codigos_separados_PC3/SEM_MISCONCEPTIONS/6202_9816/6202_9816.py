altura_bia = 1.69
taxa_bia = 0.01

altura= float(input("Digite a altura da pessoa:"))
taxa= float(input("Digite a taxa de crescimento da pessoa:"))

ano = 0

while (altura_bia>=altura) :
	ano +=1
	altura_bia = altura_bia + taxa_bia
	altura = altura +taxa
print(ano)
	