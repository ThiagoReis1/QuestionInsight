valor1=float(input("quantidade consumida:"))
metro_cubico=0.37
taxa=15.00
valor2=valor1*metro_cubico+taxa
icms=valor2*0.35
valor3=valor2+icms
print(round(valor3,2))