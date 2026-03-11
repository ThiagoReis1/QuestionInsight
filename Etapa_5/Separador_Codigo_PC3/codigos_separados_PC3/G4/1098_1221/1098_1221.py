x=int(input("Digite um numero qualquer: "))
d = x // 1000
resto_d = x % 1000
info =(d+resto_d)**2
if(x == info):
	print(info, "X atende a propriedade")

