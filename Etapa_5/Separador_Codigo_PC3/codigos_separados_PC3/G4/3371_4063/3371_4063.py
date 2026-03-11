u = input("Digite K para km ou M para milhas: ")
v = float(input("valor da medida: "))

a = u.upper()

if a =="M":
	b = 1.60934 * v
else:
	b = v/1.60934
print(round(b, 2))