produto =  (input("Codigo do produto:"))
pbolo2=5.00
psalgado2=4.00
pcapuccino2=7.50
qsb2 = float(input("Quantidade de saldago ou bolo"))
qc2 = float(input("quantidade de capuccino"))
if produto =="S":
	
	preco1= psalgado2*qsb2+qc2*pcapuccino2
	print (preco1)
else:
	preco2= pbolo2*qsb2+qc2*pcapuccino2
	print(preco2)
	
	
