consumo=float(input("consumo em minuto:"))
var=(consumo*0.28)+23
aumento=(var)*(31/100)
valor=var+aumento
print(round(valor,2))