am = float(input("Quantidade de votos Ambrosio: "))
de = float(input("Quantidade de votos Demelza: "))
s = (am+de)
pa = (am/s)*100
pd = (de/s)*100

if (am > de):
	print("Ambrosio Rutra", round(pa, 2))
else:
	print("Demelza Olecram", round(pd, 2))


