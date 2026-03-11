posicao = int(input("Digite a posicao inicial do objeto: "))
velocidade = int(input("Digite a velocidade do objeto: "))
tempo = int(input("Digite o tempo de deslocamento: "))
limite = 100
s = posicao + (velocidade * tempo)
print(s)
if velocidade > limite:
	print("ACIMA")
else:
	print("OK")