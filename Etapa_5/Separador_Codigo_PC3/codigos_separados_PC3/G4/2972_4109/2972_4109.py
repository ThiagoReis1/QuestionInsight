ss = int(input("Posicao inicial do objeto: "))
v= int(input("Velocidade do objeto: "))
t = int(input("Tempo de deslocamento: "))

s = (ss + v * t)

if (s >= 1000):
	print(s)
	print("Sim")

else:
	print(s)
	print("Nao")