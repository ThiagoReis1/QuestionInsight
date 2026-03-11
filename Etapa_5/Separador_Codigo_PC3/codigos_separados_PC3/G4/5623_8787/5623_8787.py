cond = input("digite B se for bolo, S se for salgado: ")
rango = int(input("qt de fatias: "))
capp = int(input("qt de cappu: "))
s = 4.00
b = 5.00
c = 7.50
if cond == "S" : 
   total = rango * s + capp * c
   print(round(total,2))
else:
   total = rango * b + capp * c
   print(round(total,2))



