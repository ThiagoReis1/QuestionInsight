x=input("Digite L para lanche ou S para salgado: ")
y=int(input("Quantos vai querer: "))
r=int(input("Quantos refri vai querer: "))

if(x=="L"):
	p=float(y*5 + r*4)
	print(round(p,2))
else:
			p=float(y*3.50+r*4)
			print(round(p,2))
