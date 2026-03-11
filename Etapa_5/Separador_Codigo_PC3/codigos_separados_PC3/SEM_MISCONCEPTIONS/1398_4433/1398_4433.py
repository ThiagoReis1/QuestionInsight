tempo_de_voo = float(input('minutos:'))

if(tempo_de_voo <= 200):
	custo_total = 5000 + 100*tempo_de_voo
else:
	custo_total = 8000 + 100*tempo_de_voo + 90
	
print(round(custo_total, 2))