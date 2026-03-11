pedido = input("digite o pedido L ou P :")
quant = int(input(""))
Q_refri = int(input(""))
L = quant * 6.00
P = quant * 4.50
R = Q_refri * 3.00

caso =  L + R
casob = P + R
if pedido == "L" :
	print(caso)
	
else:
	  print(casob)
   
  	
    
	  