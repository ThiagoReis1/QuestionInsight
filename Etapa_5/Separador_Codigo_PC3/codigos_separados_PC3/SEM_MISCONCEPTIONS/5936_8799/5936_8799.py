energia = float(input("Qualo o consumo de kWh? "))

pago_enrg = energia * 0.43
ilumina = 10
Total_1 = pago_enrg + ilumina

ICMS = Total_1 * 25/100

Total = Total_1 + ICMS

print(round(Total , 2))