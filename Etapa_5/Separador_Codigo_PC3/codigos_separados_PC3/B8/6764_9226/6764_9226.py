custo_fixo = 10.0
peso_pacote = float(input("digite o peso do pacote: "))

if (peso_pacote > 0) and (peso_pacote < 5): 
	peso = custo_fixo + 3.75
elif peso_pacote == 5: 
	peso = custo_fixo + 4.75
elif peso_pacote > 5:
	peso = custo_fixo + 5.75

print(round(peso, 2))
