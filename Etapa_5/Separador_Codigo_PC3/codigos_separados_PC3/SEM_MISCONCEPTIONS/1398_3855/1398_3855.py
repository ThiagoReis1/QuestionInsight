T = int(input('Tempo de voo eh igual a:'))
if (T <= 200):
	Tempo_de_Voo = (5000 + 100 * T)
else:
	Tempo_de_Voo = (8000 + 100 * 200) + (90)*( T - 200)
print(float(Tempo_de_Voo))
