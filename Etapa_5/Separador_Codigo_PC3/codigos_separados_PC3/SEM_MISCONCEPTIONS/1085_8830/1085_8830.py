notarav = float(input("insira sua nota ravenna: "))
media = notarav
prova=1

while prova < 5:
	#media = notarav
	notarav = float(input("insira a proxima nota: "))
	media = media + notarav
	prova = prova + 1
if (media/5) >= 6.0:
	print(round(media/5,2))
	print("Aprovacao")
else:
	print(round(media/5,2))
	print("Reprovacao")