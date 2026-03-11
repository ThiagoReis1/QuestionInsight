from math import*

s= str(input("Qual o seu aminoácido ?"))

#variáveis

O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794

#Aminoácidos

ALANINA = ((C * 3) + (H * 7) + (N) + (O *2))
VALINA = ((C * 5) + (H * 11) + (N) + (O * 2))
TIROSINA = ((C * 9) + (H * 11) + (N) + (O * 3))

#Condição

if (s)== ("ALANINA") or ("VALINA") or ("TIROSINA"):
			print(float(s == (round("ALANINA",2) or (round("TIROSINA",2) or (round("VALINA",2)))
		else:			
			print(s.upper() == "Dado Inválido")