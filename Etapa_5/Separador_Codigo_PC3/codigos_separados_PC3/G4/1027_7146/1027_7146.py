kwh = float(input("Digite o consumo de kWh mensal:"))
t = (kwh * 0.43) + 10.00 
tf = (t * 0.25) + t

print(round(tf, 2))