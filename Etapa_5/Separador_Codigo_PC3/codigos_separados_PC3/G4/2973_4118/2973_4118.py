s0 = int(input("Posicao inicial: "))
v  = int(input("Velocidade do objeto: "))
t  = int(input("Tempo de deslocamento: "))
s = s0 + v*t
if(v>100):
	print(s)
	print("ACIMA")
else:
	print(s)
	print("OK")
