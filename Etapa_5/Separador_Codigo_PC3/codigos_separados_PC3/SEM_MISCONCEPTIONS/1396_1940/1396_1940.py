conta = float (input("coloque o valor da conta"))
gorjeta300 = conta + conta * 10/100
gorjeta301 = conta + conta * 6/100
if (conta <= 300):
	print (round (gorjeta300,2))
if (conta >= 301):
   print (round (gorjeta301,2))