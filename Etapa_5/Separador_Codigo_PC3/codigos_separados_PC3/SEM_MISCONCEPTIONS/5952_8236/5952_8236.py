x = input("tapioca ou salgado(T ou S)")
y = int(input("quantidade de salgados ou tapiocas: "))
z = int(input("quantidade de acais: "))
total = (y * 3.5) + (z * 13)
final = (y * 5) + (z * 13)
if x == "T":
	print(round(total, 2))
else:
	print(round(final, 2))