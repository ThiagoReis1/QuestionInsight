x = int(input("qual o valor de x: "))

x1 = x // 1000
x2 = x % 1000

div1 = (x1 + x2)**2
div2 = (x1**2) + (x2**2)

if(x==div1):
	print("x atende a propriedade")	

else:
	print(div1)
	
	
	