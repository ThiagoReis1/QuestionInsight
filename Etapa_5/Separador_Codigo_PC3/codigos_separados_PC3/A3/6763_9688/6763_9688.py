# faça seu código aqui!
trf_fixa = 5.00
t = float(input("Taxa adicional:"))
total = 0

if t < 2:
	total = trf_fixa + 1.25
	
elif t == 2:
	total = trf_fixa + 2.25

else:
	total = trf_fixa + 3.25
		
print(round(total, 2))	