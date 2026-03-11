amino=input("nome do amino: ").upper()
o=15.9994
c=12.011
n=14.00674
h=1.0079
glicina=c*2+h*5+n+o*2
serina=c*3+h*7+n+o*3
if(amino=="GLICINA"):
	print(round(glicina,2))
else:
	print(round(serina,2))