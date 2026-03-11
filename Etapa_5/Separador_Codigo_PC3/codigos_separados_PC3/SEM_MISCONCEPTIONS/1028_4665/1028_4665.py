var1 = float(input("Qual o volume de agua?"))
consumo = 0.37*var1+15
total = consumo*(35/100)
total_final = consumo+total
print(round(total_final,2))
