o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079

mol = input("Digite um aminoacido: ").lower()

if(mol!="histidina" and mol!="leucina" and mol!="lisina"):
	print("Entrada:",mol)
	print("Dado Invalido")
else:
	if(mol=="histidina"):
		print(round(6*c + 10*h + 3*n + 2*o, 2))
	if(mol=="leucina"):
		print(round(6*c + 13*h + n + 2*o, 2))
	if(mol=="lisina"):
		print(round(c*6 + h*15 + n*2 + o*2, 2))