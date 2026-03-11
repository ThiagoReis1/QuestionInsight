var= float(input("valor de entrada"))

conta=  float(var*0.97) 
total = float(conta+45)
tax= float((total *42) /100)

pag=float(total+tax)
print(round(pag, 2))