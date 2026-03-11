so = int(input(" posicao inicial do objeto:"))
v = int(input("velocidade do objeto:"))
t = int(input("tempo de deslocamento:"))
lim = 100

if (v<=100):
	s = so + (v*t)
	mensagem = "OK"
	print(s)
	print(mensagem)
else: 
	s = so + (v*t)
	mensagem = "ACIMA"
	print(s)
	print(mensagem)