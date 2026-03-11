num= int(input("Informe o numero para verificacao: "))
x= (num//1000)%1000
y= num%1000
if ((x-y)**4)==(num):
	print(num)
	print("atende")
else:
	print(num)
	print("nao atende")