# Paulo Bitencourt
# 30 - 06 - 2016

Nota1 = float(input("Valor da nota 1? "))
Nota2 = float(input("Valor da nota 2? "))
Nota3 = float(input("Valor da nota 3? "))
Nota4 = float(input("Valor da nota 4? "))

total = (Nota1 + Nota2 + Nota3 + Nota4) / 4

print(round(total, 2))

if (total >= 5):
	print ("Aprovacao")
	
else:
	print ("Reprovacao")