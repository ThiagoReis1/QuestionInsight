tempo = int(input("Digite o tempo do voo: "))
lim = 200

total1 = float(20000 + 8000 + 90*(tempo-lim))
total2 = float(5000 + 100*tempo)
if(tempo > 200):
	print(round(total1,2))
else:
	print(round(total2,2))
