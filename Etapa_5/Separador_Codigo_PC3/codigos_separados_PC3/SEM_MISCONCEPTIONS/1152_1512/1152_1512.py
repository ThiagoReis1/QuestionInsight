nhb = int(input("numero de h em Bravos: "))
nhp = int(input("numero de h em Pentos: "))
nhpr = int(input("numero de h em Porto Real: "))
taxab = float(input("taxa anual em bravos: "))
taxap =float(input("taxa anual em Pentos: "))
taxapr = float(input("taxa anual em Porto Real: "))
tempo = 0

while (nhb + nhp < nhpr):
	nhb = nhb + (nhb *taxab/100)
	nhp = nhp +(nhp *taxap/100)
	nhpr = nhpr + (nhpr* taxapr/100)
	tempo = tempo +1
print(tempo)
