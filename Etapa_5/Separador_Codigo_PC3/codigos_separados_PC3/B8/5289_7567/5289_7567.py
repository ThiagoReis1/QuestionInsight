face = int(input(""))
jogadas = 0
seis = 0
while(face != -1):
	if(face == 6):
		jogadas = jogadas + 1
		seis = seis + 1
		face = int(input(""))
	elif(1 <= face <= 5):
		jogadas = jogadas + 1
		face = int(input(""))
porcentagem = seis * 100/jogadas 
print(jogadas)
print(round(porcentagem, 2))
