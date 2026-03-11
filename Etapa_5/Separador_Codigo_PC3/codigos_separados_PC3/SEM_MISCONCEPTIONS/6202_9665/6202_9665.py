altura_bia = 1.69
taxa_bia = 0.01

alt = float(input("digite a altura: "))
tx = float(input("digite a taxa: "))

ano = 0

while alt < altura_bia:
	altura_bia = altura_bia + taxa_bia
	alt = alt + tx
	ano = ano + 1
	
print(ano)