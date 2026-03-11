a = float(input("Nota 1:"))
b = float(input("Nota 2:"))
c = float(input("Nota 3:"))
d = float(input("Nota 4:"))
m = (a + b + c + d)/4
if(m >= 6):
	r = ("Aprovado")
else:
	r = ("Reprovado")
print(round(m,1))
print(r)