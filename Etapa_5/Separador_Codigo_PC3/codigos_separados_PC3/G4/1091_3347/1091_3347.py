entrada = int(input("entrada: "))

x = entrada // 100 % 100
y = entrada %100

e = (x + y)**2

if(e == entrada):
	print(entrada, "atende")
else:
	print(entrada, "nao atende")

