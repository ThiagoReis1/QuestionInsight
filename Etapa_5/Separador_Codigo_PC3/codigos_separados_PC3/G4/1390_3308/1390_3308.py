mn = int(input("digite os minutos:"))
if (mn <=100):
	print(round(mn*1.20,2))
else:
	print(round(mn*1.40 + 25,2))