tpVoo = int(input("Tempo de voo:"))

if(tpVoo <= 200):
	ct = 5000 + 100 * tpVoo
else:
	ct = 8000 + (100*200) + 90 * (tpVoo - 200)
	
print(round(ct,2))