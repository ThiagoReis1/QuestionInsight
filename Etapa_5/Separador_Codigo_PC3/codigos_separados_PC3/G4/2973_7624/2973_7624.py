s0 = int(input("posicao inicial: "))
v = int(input("velocidade: "))
t = int(input("tempo de deslocamento "))

s = s0 + v * t 

print(s)

if (v<=100):
	print("OK")
else:
	print("ACIMA")