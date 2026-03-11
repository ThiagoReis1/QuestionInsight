a=float(input("primeira compra:"))
b=float(input("segunda compra:"))
c=float(input("terceira compra:"))
limite=float(input("limite do cartao:"))
total=a+b+c
print(round(total,2))
if	(total<=limite):
	mensagem="Nao ultrapassou"
	print(mensagem)
else:
	mensagem="Ultrapassou"
	print(mensagem)