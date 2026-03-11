var = float(input("qual a quantidade de litros abastecidos: "))
tdo = (var*2.86)+50.0
icms = tdo*0.34
vt = icms+tdo
print(round(vt, 2))