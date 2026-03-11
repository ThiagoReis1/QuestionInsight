nome=input("nome do aminoacido: ").upper()
o=15.9994
c=12.011
n=14.00674
h=1.0079

if(nome == "GLICINA") or (nome=="PROLINA") or (nome == "SERINA"):
	if (nome == "CLICINA"):
		soma = (c*2)+(h*5)+n+(o*2)
		print(round(soma,2))
	elif (nome == "PROLINA"):
		soma = (c*5)+(h*10)+n+(o*2)
		print(round(soma,2))
	elif (nome == "SERINA"):
		print(round((c*3)+(h*7)+n+(o*2),2))
	
		print(round(soma,2))
else:
	print("Entrada:",nome)
	print("Dado Invalido")