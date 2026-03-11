x = float(input("Nota1: "))
y = float(input("Nota2: "))
z = float(input("Nota3: "))
k = float(input("Nota4: "))
t = float(input("Nota5: "))
media = ((x + y + z + k + t)/(5))
if(media >= 7):
	print(round(media,2 ))
	print("Aprovacao")
else:
	print(round(media,2 ))
	print("Reprovacao")
