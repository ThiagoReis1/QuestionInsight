aminoacido = input("Digite o nome do aminoacido: ").upper()

O = 15.9994
C = 12.011
N =14.00674
H = 1.0079
	
if(aminoacido == "Prolina") or (aminoacido == "GLICINA") or (aminoacido == "Serina"):
	if(aminoacido == "GLICINA"):
		p = (C*2)+(H*5)+(N*1)+(O*2)
		print(p(round,2))
		if(aminoacido == "Prolina"):
			p = (C*5)+(H*10)+(N*1)+(O*2)
			print(p(round,2))
			if(aminoacido== "Serina"):
				p = (C*3)+(H*7)+(N*1)+(O*3)
				print(p(round,2))
else:
	print("Dado Invalido")
				

	