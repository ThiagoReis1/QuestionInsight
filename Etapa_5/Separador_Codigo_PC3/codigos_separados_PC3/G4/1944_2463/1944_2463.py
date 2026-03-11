nome= input("Nome do aminoácido: ")
o= 15.9994
c= 12.011
n= 14.00674
h= 1.0079
if(nome.lower() == "leucina"):
	print(round((6*c)+(13*h)+n+(o*2),2))
if(nome== "lisina"):
	print(round((6*c)+(15*h)+(n*2)+(o*2),2))
