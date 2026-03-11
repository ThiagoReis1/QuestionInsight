s = input("Informe a sequencia de ids de notas: ")
vet = s.split(",")

ids = "CDVU"
notas = [100, 50, 20, 10]
cont_notas = [0, 0, 0, 0]

for i in range(len(vet)):
	cont_notas[ids.find(vet[i])] += 1
	
print(str(cont_notas).replace(",", ""))