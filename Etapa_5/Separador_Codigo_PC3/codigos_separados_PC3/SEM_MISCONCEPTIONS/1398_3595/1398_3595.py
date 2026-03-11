tempoVoo = float(input())

if(tempoVoo <= 200):
	custo = 5000+tempoVoo*100
else:
	excedente = tempoVoo-200
	custo = 8000+100*200+90*excedente

print(round(custo, 2))
