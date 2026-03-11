idade_esp = int(input("Insira a idade do espectador: "))
ingresso = 20

if idade_esp < 12:
	ingresso += 1.25
elif idade_esp == 12:
	ingresso += 2.25
elif idade_esp > 12:
	ingresso += 3.25

print(round(ingresso, 2))