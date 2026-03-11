umd= input("K para quilometros e M para milhas: ").upper()
vm= float(input("Valor da medida:"))

if (umd == "K"  ):
   mi= vm / 1.60934
   print(round(mi,2))
else:
   km= vm * 1.60934  
   print(round(km,2))