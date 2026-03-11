# peso molecular
aminoacido = input( " nome do aminoacido ").upper()

O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

Glicina = (C*2)+(H*5)+(N)+(O*2)
Serina = (C*3)+(H*7)+(N)+(O*3)

if(aminoacido == "GLICINA"):
	print(round(Glicina,2))
else:
	print(round(Serina,2))

	