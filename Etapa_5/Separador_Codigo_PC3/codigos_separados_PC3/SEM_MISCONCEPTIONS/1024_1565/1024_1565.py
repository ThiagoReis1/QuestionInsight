#Arleson Castro
#Lab 01 - Av 01

comprimento = float(input("lado a:"))
comprimento2 = float(input("lado b:"))
comprimento3 = float(input("lado c:"))
custo = float(input("metro:"))
perimentro = comprimento + comprimento2 + comprimento3
total = perimentro * custo

print(round(total,2))