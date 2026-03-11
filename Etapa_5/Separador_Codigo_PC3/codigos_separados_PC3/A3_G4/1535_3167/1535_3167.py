x = float(input("defina o numero x: "))
k = int(input("defina a quantidade de termos: "))
cont = 0
var = 1

while(x >= -1 and x<= 1):
	var = x - ((x**3)/3) + ((x**5)/5) - ((x**7)/7) + ((x**9)/9)
	if(k > 0):
		cont = var + 1
print(round(cont , 6))