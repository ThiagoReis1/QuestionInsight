kg=float(input("Quantos quilos a ser transportado:  "))
frete=(kg*43.21)+25.0
icms=(frete*62.0)/100.0
fretetotal=(frete+icms)
print("O frete custara R$") 
print(fretetotal)
