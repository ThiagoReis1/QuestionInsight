tag = input("Etiqueta: ").upper()
i = 0
not_vogal = 0

while i < len(tag):
	if tag[i] != "A" and tag[i] !="E" and tag[i] !="I" and tag[i]!="O" and tag[i]!="U":
		not_vogal = not_vogal + 1
	i = i + 1

print(round(len(tag) * 0.15 + not_vogal * 0.02,  2))