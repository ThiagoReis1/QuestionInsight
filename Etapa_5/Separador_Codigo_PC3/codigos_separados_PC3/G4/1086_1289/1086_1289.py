#Bianca Daniele (21602286)
x=float(input("insira nota 1: "))
y=float(input("insira nota 2: "))
z=float(input("insira nota 3: "))
m=(x+y+z)/3
print(round(m,1))
if m>=7:
	print("Aprovado")
else:
	print("Reprovado")