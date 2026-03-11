mino = input("Digite o seu aminoacido: ")
o=15.9994
c=12.011
n=14.00674
h=1.00794

if(mino=="ALANINA"):
		x= c*3+h*7+n+o*2
		x=round(x,2)
elif(mino=="VALINA"):
	x=c*5+h*11+n+o*2
	x=round(x,2)
elif(mino=="TIROSINA"):
	x=c*9+h*11+n+o*3
else:
	x = "Dado invalido"
print(x)