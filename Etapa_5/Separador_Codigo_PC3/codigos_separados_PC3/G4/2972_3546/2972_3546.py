s0 = int(input("posicao inicial: "))
v = int(input("velocidade: "))
t = int(input("tempo: "))

s = s0 +v*t

print(s)

if(s>1000):
	print("Sim")
else:
	print("Nao")