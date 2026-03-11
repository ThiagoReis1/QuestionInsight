So = int(input("A posicao inicial do objeto: "))
v = int(input("A velocidade do objeto (m/s): "))
t = int(input("O tempo de deslocamento: "))

S = So + v * t 
print(S)

if v <= 100 : 
	mensagem = "OK"
	print(mensagem)

if v > 100: 
	mensagem = "ACIMA"
	print(mensagem)