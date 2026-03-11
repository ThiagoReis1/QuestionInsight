nome = input("aminoacido:")
o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794
GLUTAMINA = c*5 + h*8 + n*1 +o*4
SERINA = c*3 + h*7 + n + o*3	
TREONINA = c*4 + h*9 + n + o*3
if(nome=="GLUTAMINA"):
	print(round(GLUTAMINA,2))
elif(nome=="SERINA"):
	print(round(SERINA,2))
elif(nome=="TREONINA"):
	print(round(TREONINA,2))
else:
	print("Entrada: X")
	print("Dado Invalido.")
