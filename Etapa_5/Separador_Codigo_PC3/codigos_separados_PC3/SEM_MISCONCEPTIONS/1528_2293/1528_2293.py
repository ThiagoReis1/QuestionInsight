forcaretirada = int(input(" "))
pontosiniciais = int(input(""))
pontosrecuperados = int(input(" "))
f = pontosiniciais 
r =  0
while (f > 0):
	pi = f - 5*forcaretirada
	f = pi + pontosrecuperados
	r = r + 1 
print(r)