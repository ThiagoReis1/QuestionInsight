v = int(input("Insira o numero de copias iniciais do virus no sangue: "))
l = int(input("Insira o numero de  leucocito inicial: "))
taxav = int(input("Insira a taxa de crescimento do virus: "))
taxal = int(input("Insira a taxa de crescimento de leucocitos: "))

tv = taxav/100
tl = taxal/100
v = v + (v * tv)
l = l + (l * tl)
i = 1
while(v >= 2 * l):
	v = v + (v * tv)
	l = l + (l * tl)
	i = i + 1
print(i)