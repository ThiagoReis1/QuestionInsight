tempo= int(input("tempo em meses:  "))
valor1= float(1500)
valor2= float(1042000)
taxa=((valor2**(1/tempo)/valor1**(1/tempo))-1)

if(taxa<= 0.01):
   mensagem="Real"
else:
	mensagem="Irreal"
print(round(taxa,5))
print(mensagem)

