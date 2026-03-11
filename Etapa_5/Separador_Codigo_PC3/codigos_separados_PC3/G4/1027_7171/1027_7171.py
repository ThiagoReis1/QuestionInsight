#Conta de Energia
custo= 0.43 # Custo do KWh
ilum= 10.00

tax= float( input("Digite o consumo de energia:"))
calc= ((tax * custo) + ilum) * 1.25
print( round( calc, 2))
