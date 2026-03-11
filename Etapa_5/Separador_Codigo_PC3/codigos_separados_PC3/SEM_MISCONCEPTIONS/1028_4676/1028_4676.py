m= float(input("O volume de agua consumida durante certo mes: "))
fixo=15
imposto=35/100*(15+0.37*m)

total=fixo+m*0.37+imposto

print(round(total, 2))