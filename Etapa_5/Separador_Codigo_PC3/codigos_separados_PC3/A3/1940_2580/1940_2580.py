a = input("escreva o nome do aminoacido: ")
g = "glutamina".upper()
peso_g= ((5*12.011) + (8*1.00794)+ (1*14.0067) +(4*15.9994))
t = "treonina".upper()
peso_t= ((4*12.011) + (9*1.00794) +(1*14.0067 +3*15.9994))
if (a == g):
	print(round(peso_g, 2))
else:
	print(round(peso_t, 2))