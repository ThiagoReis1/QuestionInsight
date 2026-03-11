# faça seu código aqui!
q = int(input("Quantidade : "))
custo = 32.90

if q <= 3 :
	var = q * custo

else :
	var =  (((q * custo) * 0.2) - (q * custo)) * -1
	
print(round(var,2))