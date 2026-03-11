tirados = int(input())
inicial = int(input())
recuperados = int(input())
jogadas = 0
while(jogadas<0):
	ln = (inicial + (jogadas * recuperados)) - (jogadas * tirados)
	jogadas = jogadas + 1
	print(ln)