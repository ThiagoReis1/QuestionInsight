q= float(input("quantidade de horas:"))

media= 50.00 * 20
if q > 20:
   pagamento= media + ((q - 20) * 70.00 )
   print(round(pagamento,2))
else:
   pagamento= q * 50.00
   print(round(pagamento,2))