#victor do vale moreira
#av.02
#14/07/2016

n1 = float(input("nota primeira prova:"))
n2 = float(input("nota segunda prova:"))
n3 = float(input("nota terceira prova:"))

media = (n1 + n2 + n3) / 3

if (media >= 7):
	print(round (media , 1))
	print("Aprovado")
else:
	print(round(media, 1)) 
	print("Reprovado")