consumo = float(input("consumo de agua: "))
custo = (consumo * 0.37) + 15.00
custototal = custo + (custo * 35/100)
print(round(custototal,2))