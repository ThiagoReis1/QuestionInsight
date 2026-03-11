#JoséRoberto

nota1=float(input("digite nota 1:"))
nota2=float(input("digite nota 2:"))
nota3=float(input("digite nota 3:"))
nota4=float(input("digite nota 4:"))	
nota5=float(input("digite nota 5:"))
	
mf=(nota1+nota2+nota3+nota4+nota5)/5

print(round(mf,2))

if(mf>=7):
	print("Aprovacao")
	
else:
	print("Reprovacao")