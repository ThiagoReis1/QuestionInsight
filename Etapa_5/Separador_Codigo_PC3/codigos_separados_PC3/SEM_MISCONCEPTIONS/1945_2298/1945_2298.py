nomedoaminoacido= input("escreva o nome do aminoacido:").lower

O= 15.9994
C= 12.011
N= 14.0067
S= 32.066
H= 1.00794

Aspartato= float(round((C * 4)+(H * 6)+(N * 1)+(O * 4),2))
Cisteina= float(round((C * 3)+(H * 7)+(N * 1)+(O * 2)+(S * 1),2))

if (nomedoaminoacido == "Aspartato"):
   print(round(Aspartato,2))
else:
	print(round(Cisteina,2))
	
	
