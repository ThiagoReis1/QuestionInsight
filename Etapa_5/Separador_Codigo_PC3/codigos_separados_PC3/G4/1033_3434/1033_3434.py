peso = float(input("peso da cargo: "))
k = 43.21
t = 25
icms = ((peso*k)+t)*62/100
valor = ((peso*k)+t)+icms
print(round(valor,1))