x = int(input(" digite o valor de x: "))

if x%47 == 0 :
	resto = x // 47
	mensagem = "sim"
	
else:
	resto = x%47
	mensagem = "nao"
	
print(resto)
print(mensagem)