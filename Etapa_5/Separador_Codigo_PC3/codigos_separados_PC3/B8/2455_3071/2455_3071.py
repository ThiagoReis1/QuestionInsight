nivel = int(input("Digite: "))
horas = int(input("Digite: "))

if (nivel == 1):
	s = (horas * 12)
	print(round(s, 2))
elif (nivel == 2):
	s = (horas * 17)
	print(round(s, 2))
elif (nivel == 3):
	s = (horas * 25)
	print(round(s, 2))