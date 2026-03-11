valor = int(input("informe um valor de 6 digitos :"))

a = valor // 1000
b = valor % 1000

c = (a - b)**4
print(valor)

if(c == valor):
	print("atende")

else:
	print("nao atende")




