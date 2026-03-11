entrada = int(input("valor : "))
x = entrada // 1000 % 1000
y = entrada % 1000

e= (x + y)**2

if(e == entrada):
	print("atende" , entrada)
	
else:
	print("nao atende" , entrada)
