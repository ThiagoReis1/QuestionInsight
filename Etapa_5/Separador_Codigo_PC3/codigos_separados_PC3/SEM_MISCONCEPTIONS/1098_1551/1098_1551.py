numb = int(input("insira um numero com 6 digitos: "))
numbx = 234256
numb1 = int(numbx %1000)
numb2 = int(numbx//1000)
equacao = (numb1 - numb2)**4
if(numb == equacao):
	print("X atende a propriedade")
else:
	print(equacao)