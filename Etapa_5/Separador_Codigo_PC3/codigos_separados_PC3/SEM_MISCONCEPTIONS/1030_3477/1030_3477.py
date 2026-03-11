minutos = float(input("minutos excedente: "))
valor = 45+(0.97 * minutos)  
icms = valor * 42/100 
valor_total= valor + icms
print(round(valor_total,2))		