x = float (input ("Consumo de chamadas (em minutos) por mes? "))
y = (0.28 * x) + 23.00
z = (y * 31) / 100
a = y + z
print (round (a, 2))