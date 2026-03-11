quantidade=float(input("Quantidade de litros abastecido:"))
litro= 2.86
oleo= 50.00

conta=quantidade*litro+oleo
icms= conta * 0.34

total=conta + icms

print(round(total,2))
