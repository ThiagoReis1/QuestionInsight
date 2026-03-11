age = int(input("em que ano vc nasceu? "))
country = input("digite B para brasil or I for england: ").upper()
year = 2023 - age
if country == "B":
	if year >= 18:
		print("sim")
		print(year - 18)
	else:
		print("nao")
		print(18 - year)
elif country == "I":
	if year >=17:
		print("sim")
		print(year - 17)
	else:
		print("nao")
		print(17 - year)