voo = float(input("tempo de voo: "))
if (voo <= 200):
	msg = 5000 + (100*voo)
else:
	msg = 8000 + (100*200) + (voo-200) * 90
print(round(msg,2))