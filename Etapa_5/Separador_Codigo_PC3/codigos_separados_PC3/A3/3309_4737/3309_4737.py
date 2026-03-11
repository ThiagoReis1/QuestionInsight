peso=float(input("Peso da mercadoria: "))
v_kilo=43.21
taxa=25.00
carga=(v_kilo*peso)+taxa
#imposto sobre o valor total
icms=62
total=carga+((carga*62)/100)
print(round(total,1))