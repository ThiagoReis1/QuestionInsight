import math
raio_da_fazenda= float( input ("digite o raio da fazenda"))
custo_metro= float (input ("digite o custo"))
area= (math.pi*raio_da_fazenda**2)
custo_total=  (area*custo_metro)
print(round(custo_total,2))

