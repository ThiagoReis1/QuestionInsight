n = int(input("digite um numero inteiro: "))

if (n%43 == 0):
	imprimir = n//43
	mensagem = "sim"
	
else:
	imprimir = n%43
	mensagem = "nao"
	
print(imprimir)
print(mensagem)