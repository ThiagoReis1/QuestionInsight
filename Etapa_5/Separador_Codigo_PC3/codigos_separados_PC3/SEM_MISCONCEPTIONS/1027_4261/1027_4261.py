varenergia = float(input("Quantos kwh foram consumidos?"))
varconta = (varenergia * 0.43 + 10)
total = (varconta * (25/100)+ varconta)
print(round(total,2))
