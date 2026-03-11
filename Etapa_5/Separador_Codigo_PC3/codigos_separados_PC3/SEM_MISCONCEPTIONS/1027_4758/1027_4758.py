kwh = float(input("quantos kwh foram consumidos: "))
conta = kwh*0.43+10
por = 25/100
total = (conta+(conta*por))
print (round(total,2))