pc = 45.00
tpm = 0.97
m = float(input("Numero de minutos excedentes: "))
VP = (pc + tpm*m)
P = VP * (42/100) #42% do valor do pagamento
VT = VP + P #valor total vai ser a soma do valor do pagamento com a porcentagem
print(round(VT, 2))