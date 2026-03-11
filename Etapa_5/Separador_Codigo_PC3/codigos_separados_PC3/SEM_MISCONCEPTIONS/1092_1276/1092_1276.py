x = int(input("Digite um numero: "))
c = x // 100
restoc = x % 100
d = restoc//10
restod = restoc%10
u = restod 
cubos = c**3 + d**3 + u**3
if (cubos == x):
	print(x, "atende a propriedade")
else:
	print(cubos)