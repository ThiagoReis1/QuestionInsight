totalkwh = float(input("consumo mensal: "))

conta = ((0.43 * totalkwh)+10)
totaldaconta = (conta + (0.25*conta))
print(round(totaldaconta,2))