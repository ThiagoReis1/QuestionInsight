minutos_exedente=float(input(""))
conta_inicial = 45
minuto_extra = 0.97
icms =0.42*((minuto_extra * minutos_exedente)+45)
conta_final = ((minuto_extra * minutos_exedente)+45)+icms

print(float(round(conta_final,2)))