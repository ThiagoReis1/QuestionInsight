d = input("Bastardo:")
if d==Snow:
	msg = "Norte"
elif d==Stone:
	msg = "Vale"
elif d==Rivers:
	msg = "Terras Fluviais"
elif d==Storm:
	msg = "Terras da Tempestade"
elif d==Sand:
	msg = "Dorne"
elif d==Pyke:
	msg = "Ilhas de Ferro"
elif d==Flowers:
	msg = "Campinas"
elif d==Hill:
	msg = "Terras Ocidentais"
elif d==Waters:
	msg = "Terras da Coroa"
else:
	msg = "Entrada",d,"Invalida"
print(msg)
