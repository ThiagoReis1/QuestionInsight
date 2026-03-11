agua=float(input("volume consumido:"))
subt=float(agua*0.37)+15
icms=float((35/100)*subt)
tarifa=subt+icms
print(round(tarifa,2))