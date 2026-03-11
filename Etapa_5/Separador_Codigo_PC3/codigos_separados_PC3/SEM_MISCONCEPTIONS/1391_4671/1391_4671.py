kw=float(input("kWh consumido: "))

if (kw<=150):
	empresa=0.6*kw+5
else:
	empresa=0.75*kw+16
print(round(empresa,2))