casa = input("casa: ")
a = Baratheon
b = Tagaryen
c = Tyrell
d = Stark
e = Lannister
f = Greyjoy
g = Tully
h = Arryn
i = Martell
if (casa == a):
	regiao = "Ponta Tempestade"
elif (casa == b):
	regiao = "Ilha do dragao"
elif (casa == c):
	regiao = "Campina"
elif (casa == d):
	regiao = "Winterfell"
elif (casa == e):
	regiao = "Rochedo Casterly"
elif (casa == f):
	regiao = "Pyke"
elif (casa == g):
	regiao = "Correrio"
elif (casa == h):
	regiao = "Ninho da Aguia"
elif (casa == i):
	regiao = "Dorne"
	print(regiao)
else:
	regiao = "invalida"
print("Entrada", casa, "invalida")	
