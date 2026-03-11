acai = int(input())
salgado = int(input())
dinheiro = float(input())

valorpago1 = (acai/1000)*24
valorpago2 = salgado*3

if (dinheiro - (valorpago1 + valorpago2) >= 0):
	print (round(valorpago1 + valorpago2,2))
	print ("Sim")
else: 
	print (round(valorpago1+valorpago2,2))
	print ("Nao")