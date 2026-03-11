valor=float(input("valor de encomenda"))
taxa= 12.0
imposto = valor * 81/100
valortotal= valor + taxa + imposto
print(round(valortotal, 2))