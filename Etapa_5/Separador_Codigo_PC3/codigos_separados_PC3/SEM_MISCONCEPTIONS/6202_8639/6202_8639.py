altura_bia = 1.69
taxa_bia = 0.01
cont=0

altura= float(input("Digite a altura: "))
taxa= float(input("Digite a taxa: "))

while altura<= altura_bia:
	altura= altura +taxa
	altura_bia= altura_bia+ taxa_bia
	cont= cont+1
print(cont)