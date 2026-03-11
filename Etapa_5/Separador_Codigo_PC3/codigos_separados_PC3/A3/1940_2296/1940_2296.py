nomedoaminoacido=input("escreva o nome do aminoácido:").upper

O = float (15.9994)
C = float (12.011)
N = float (12.0067)
H = float (1.00794)

Glutamina= float(round((C * 5)+(H * 8)+(N*1)+(0*4),2))
Treonina= float(round((C * 4)+(H * 9)+(N*1)+(0*3),2))

if (nomedoaminoacido=="Glutamina"):
	mensagem=print(Glutamina)
else:
	print(round,(Glutamina),2)
	