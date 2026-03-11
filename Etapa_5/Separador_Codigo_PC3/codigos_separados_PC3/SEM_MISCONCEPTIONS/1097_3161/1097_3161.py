valor= int(input("forneca um numero: "))
a= valor // 1000
b= valor % 1000

if((a-b)**2 == valor):
	print("atende")
else:
	print("nao atende")
print(valor)