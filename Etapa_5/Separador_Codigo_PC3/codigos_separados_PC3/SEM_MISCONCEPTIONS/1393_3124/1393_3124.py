peso = float(input(""))
taxa = 60.00
if (peso<=4999.9):
    valor = peso*0.05
else:
    valor = peso*0.04 + taxa 
print(round(valor,2))