numero = int(input("Informe um numero:" ))
x = numero //10000
x1 = numero % 10000
y = x1 // 100
y1 = x1 % 100
result = (x**3 + y**3 + y1**3) 
if result == numero:
	print  ( numero, "atende a propriedade")
else:
	print (result)