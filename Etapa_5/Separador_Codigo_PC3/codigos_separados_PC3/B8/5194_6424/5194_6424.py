nivel = str(input()).upper()
v = float(input())
if nivel == 'A':
	print('Classe: Jounin')
	valor = v * (1-0.22)
elif nivel == "B":
	print("Classe: Chunin")
	valor = v * (1-0.15)

print(round(valor,2))