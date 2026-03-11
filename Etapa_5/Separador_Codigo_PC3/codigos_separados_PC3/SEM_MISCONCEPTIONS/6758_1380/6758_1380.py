# faça seu código aqui!

dias = int(input("Informe a quantidade de dias: "))
custo_total = dias * 100.0
vet_taxas = [15, 12, 10]

if (dias <= 7):
	custo_total += vet_taxas[dias//7]
else:
	custo_total += vet_taxas[2]

print(round(custo_total, 2))