altura_luna = 1.65
taxa_luna = 0.02
altura_alguem = float(input("altura inicial: "))
taxa_alguem = float(input("taxa de crescimento: "))
anos = 0

while altura_luna > altura_alguem:
	if taxa_alguem > taxa_luna:
		altura_alguem = altura_alguem + taxa_alguem
		altura_luna = altura_luna + taxa_luna
		anos = anos + 1
	else:
		taxa_alguem = float(input("taxa de crescimento invalida, por favor insira uma taxa maior que 0.02:"))
print(anos)