valor= int(input("infome o numero: "))

a= valor // 1000
b= valor % 1000
xablau=((a - b)**2)

if(xablau == valor):
	print("atende")
else:
	print("nao atende")
print(valor)
	


