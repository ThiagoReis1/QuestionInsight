compra1=float(input())
compra2=float(input())
compra3=float(input())
limite=float(input())

media=(compra1+compra2+compra3)

print(round(media, 2))

if media<=limite:
	mensagem="Nao ultrapassou"
	print(mensagem)
else:
	mensagem="Ultrapassou"
	print(mensagem)
	

