so = int (input("Digite a posicao inicial do objeto (m): "))
v = int (input("Digite a velocidade do objeto (m/s): "))
t = int (input("Digite o tempo de deslocamento (s): "))

s = so+(v*t)

if(v<=100):
	print(s)
	print("OK")
	
else:
	print(s)
	print("ACIMA")