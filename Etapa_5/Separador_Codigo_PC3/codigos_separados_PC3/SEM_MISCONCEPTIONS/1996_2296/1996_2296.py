n= (input("Digite o nome do aminoácido: ".lower()))
O= 15.9994
C= 12.011
N= 14.0067
S= 32.066
H= 1.0079

Aspartato= (C*4)+(H*6)+(N)+(O*4) 
Fenilanina= (C*9)+(H*11)+(O*2)+(S)
Tirosina= (C*9) + (H*11) + (N) + (O*3)

if(n == "Aspartato"):
	print(round(Aspartato,2)
elif(n =="Fenilanina"):
	print(round(Fenilanina,2))
elif(n =="Tirosina"):
	print(round(Tirosina,2))
else:
	print()

