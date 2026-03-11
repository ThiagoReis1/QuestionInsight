peso=float(input("peso do saco: "))
quantia=float(input("quantia diaria de racao: "))

quantia_semanal=quantia*7
resto= peso-quantia_semanal

print(round(resto,2))