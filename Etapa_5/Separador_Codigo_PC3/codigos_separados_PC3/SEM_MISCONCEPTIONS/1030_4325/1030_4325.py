#A qnt de minutos excedentes
consumo = float(input("Quantidade de minutos utilizados:"))
vlr_pago = (45+(0.97*consumo))*1.42
#Valor pago
print(round(vlr_pago,2))	  