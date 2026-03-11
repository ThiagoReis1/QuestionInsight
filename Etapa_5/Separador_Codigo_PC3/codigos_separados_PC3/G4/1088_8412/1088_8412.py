not1 = float(input("insira a nota: "))
not2 = float(input("insira a nota: "))
not3 = float(input("insira a nota: "))
not4 = float(input("insira a nota: "))
not5 = float(input("insita a nota: "))

media = (not1 + not2 + not3 + not4 + not5) / 5

print(round(media, 2))
		
if media >= 7.0:
	mensagem = 'Aprovado'
	print(mensagem)
else:
	mensagem = 'Reprovado por nota'
	print(mensagem)