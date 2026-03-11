#valor usuario
numero=int(input("numero"))

numero1=numero//1000
sub=numero%1000
calculo=(numero1-sub)**4
if(calculo == numero):
	print(numero)
	print("atende")
else:
	print(numero)
	print("nao atende")