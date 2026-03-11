preco = float(input("preco do valor integral do ingresso"))
psi = preco - (preco *(60/100))
vt = preco + psi

print(round(preco,2))
print(round(psi,2))
print(round(vt,2))