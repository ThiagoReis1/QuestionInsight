x = input("T ou S:")
y = float(input("Quantidade de tapioca ou salgado:"))
z = float(input("Quantidade de acai:"))

t = 4.50
s = 5.0
a = 12.0
va = a*z
if x == "S" :
	v = s*y
else:
	v = t*y
	
print(va+v)