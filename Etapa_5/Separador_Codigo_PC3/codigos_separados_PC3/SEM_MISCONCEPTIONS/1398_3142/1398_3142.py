# tempo de voo
tempo = float(input("Qual o tempo total de voo? "))

if (tempo <= 200):
	custototal = 5000 + (100 * tempo)
else:
	custototal = (8000 + (100 * 200)) + ((tempo - 200) * 90)

print(round(custototal , 2))