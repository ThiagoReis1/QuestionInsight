#Valor Integral do Ingresso
vii = float(input())

print(round(vii,2))
		
#Preço do Segundo Ingresso d = Desconto
d = 60/100
psi =	vii - (vii * d)
		
print(round(psi,2))		
		
#Valor a ser pago
vt = psi + vii
print(round(vt,2))