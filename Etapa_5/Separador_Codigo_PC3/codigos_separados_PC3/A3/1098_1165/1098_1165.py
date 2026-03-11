x = int(input("insira um numero com 6 digitos: "))
numb1 = int(x // 234256)
numb2 = int(x%234256)
equacao = (num1 - numb2)**4
if(x == equacao):
	print("X atende a propriedade")
else:
	print(equacao)