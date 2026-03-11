pontosdevida = int(input("qual a quantidade de pontos: "))
v1 = int(input(" "))
v2 = int(input(" "))
v3 = int(input(" "))
n = v1 + v2 + v3
perde = 10 * n
m = (pontosdevida - perde)
if ( m > 0):
	print(m)
	print("VIVO")
else :
	print("0")
	print("MORTO")