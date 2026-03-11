rer = input("dados: ")
biscoito = 0
cereais = 0
lata = 0
i = 0
c = 1
while i < len(rer):
	if rer[i] == "B":
		c =  c + 3.75
		biscoito += 1
	if rer[i] == "C":
		c = c + 7.90
		cereais += 1
	if rer[i] == "E":
		c = c + 9.85
		lata += 1
	i = i + 1


print(round(c, 2)-1,biscoito,cereais,lata)