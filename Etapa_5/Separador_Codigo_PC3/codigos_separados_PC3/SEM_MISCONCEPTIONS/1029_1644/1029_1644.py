quantosminutos=float(input("Quantos minutos foram usados?"))
minuto= 0.28
valorfixo= 23.00
valoricms= (quantosminutos*minuto+valorfixo)*0.31
valoraserpago=(quantosminutos*minuto+valorfixo)+valoricms
print(round(valoraserpago,2))

