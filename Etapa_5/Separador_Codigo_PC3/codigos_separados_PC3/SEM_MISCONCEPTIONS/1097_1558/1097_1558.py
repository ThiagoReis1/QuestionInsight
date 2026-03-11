numero = int(input("digite um numero"))
subtraendo = numero % 1000
minuendo = numero // 1000
resultado = (minuendo - subtraendo) ** 2 
if (minuendo - subtraendo) ** 2 == numero:
	print (numero, "atende a propriedade")
else:
	print (resultado)