qntmin= float(input("quantidade de minutos excedentes: "))

plano= qntmin* 0.97 + 45

imposto= plano* 0.42 
total= imposto+plano

print(round(total, 2))
