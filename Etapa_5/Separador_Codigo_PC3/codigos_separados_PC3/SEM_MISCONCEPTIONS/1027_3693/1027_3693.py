kwh= float(input("digite consumo: "))
ce=0.43
vf=10.00
percentual=25/100
total=kwh*ce+vf
imposto=total*percentual
conta_total=total+imposto
print(round(conta_total, 2))

