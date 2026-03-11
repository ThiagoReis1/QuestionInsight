tv = float(input("tempo de voo:"))

if(tv <= 200):
	custo = 5000 + (100*tv)
else:
	custo = 8000 + 20000 + (90 *(tv - 200))
print(custo)
	

