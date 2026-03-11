alt = float(input("altura em metro: "))
sexo = input("em M ou F: ")
M = homem
F = mulher
#invalidos
if (alt < 1,0) and (alt > 2,5):
	print("altura invalida")
if(homem != "M") and (mulher != "F"):
	print("codigo invalido de sexo")
#Validos
if (alt > 1,0) and (alt < 2,5) and (homem == "M") and (mulher == "F"):
	M = (72,7 * alt) - 58
    print(round(M, 2)
	F = (62,1 * alt) - 44,7
    print(round(F, 2)
