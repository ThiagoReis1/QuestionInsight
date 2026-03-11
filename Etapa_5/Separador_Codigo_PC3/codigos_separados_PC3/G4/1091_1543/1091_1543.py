#vanessa Franclin Garcia
#matricula - 21602343
#AV 02 - exer 02

num = int(input("Digite um numero: "))

n1 = num//100
n2 = num%100

x = (n1+n2)**2
if(num == x):
	print(num,"atende a propriedade")
else:
	print(x)