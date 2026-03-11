s0= int(input("posicao inicial: "))
v = int(input("velocidade: "))
t = int(input("tempo: "))
s = s0+v*t
if (v <= 100):
	print(s)
	print("OK")
else:
	print(s)
	print("ACIMA")