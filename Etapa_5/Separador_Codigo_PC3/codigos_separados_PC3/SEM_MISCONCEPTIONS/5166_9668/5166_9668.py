peso_racao= float(input("qual o peso da racao?"))

quant_diaria= float(input("qual a quantidade diaria de racao?"))

restante= peso_racao - ( quant_diaria * 5)

print(round(restante, 2))