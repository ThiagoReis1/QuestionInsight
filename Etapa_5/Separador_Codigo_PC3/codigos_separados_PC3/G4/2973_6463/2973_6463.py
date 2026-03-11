pos_i = int(input("posicao inicial: "))
vel = int(input("qual a velocidade: "))
temp = int(input("qual o tempo: "))

s = pos_i + (vel*temp)

if vel <= 100:
	print(s)
	print("OK")
else:
	print(s)
	print("ACIMA")