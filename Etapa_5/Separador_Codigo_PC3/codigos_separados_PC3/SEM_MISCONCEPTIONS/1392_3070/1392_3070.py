consumo_agua = int(input("consumo de agua: "))
taxa = 30
if (consumo_agua >= 10):
	print(round(taxa + (consumo_agua * 3.5), 2))
else:
	print(round(taxa + (consumo_agua * 3), 2))
