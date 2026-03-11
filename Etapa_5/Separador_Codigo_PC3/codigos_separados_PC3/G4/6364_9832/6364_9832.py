try :
	v = int(input("Digite um numero: "))
	
except ValueError :
	print("Digite um numero!")
	
else :
	if ( v >= 3 ) :
		for i in range(v,2,-1) :
			print(i)
		print("Fim da contagem regressiva!")
		
	else :
		for i in range(v,4,1):
			print(i)
		print("Fim da contagem regressiva!")