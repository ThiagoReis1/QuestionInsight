aminoacido = (input("Informe o nome do aminoacido: "))

x = aminoacido.lower()
o = 15.9994
c = 12.011
n =14.0067
s = 32.066
h = 1.0079
if (x != "aspartato" and x != "fenilalanina" and x !="tirosina"):
	print("Entrada:",aminoacido)
	print("Dado Invalido")
elif (x=="aspartato"):
	peso = (4*c)+(6*h)+(o*4)+n
	print(round(peso,2))
elif (x=="fenilalanina"):
	peso = (9*c)+(11*h)+(2*o)+s
	print(round(peso,2))
elif (x=="tirosina"):
	peso = (9*c)+(11*h)+(o*3)+n
	print(round(peso,2))
	