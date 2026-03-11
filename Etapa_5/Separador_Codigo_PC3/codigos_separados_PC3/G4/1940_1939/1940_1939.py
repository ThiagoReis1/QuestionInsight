nome= input("").upper()

O= 15.9994
C= 12.011
N= 14.0067
H= 1.00794

if ( nome == "GLUTAMINA" ):
	glutamina= (C*5) + (H*8)+ (N*1)+ (O*4)
	print(round(glutamina,2))
else:
	treonina= (C*4)+(H*9)+(N*1)+(O*3)
	print(round(treonina,2))


