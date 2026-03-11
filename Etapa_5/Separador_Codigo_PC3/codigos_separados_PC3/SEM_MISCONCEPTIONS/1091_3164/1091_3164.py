valor=int(input("Informe um numero: "))
a=valor//100
b=valor%100
if valor==((a+b)**2):
	print(valor)
	print("atende")
else:
	print(valor)
	print("nao atende")