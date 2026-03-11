preco= float(input('preco:'))
codigo= int(input('codigo:'))

if codigo==1:
	v= round((preco-preco*40/100)+preco*(10/100),2)
	print(v)
else:
	if codigo==2:
		v= round((preco-preco*40/100)+preco*(8/100),2)
		print(v)
	else: 
		if codigo==3:
			v= round((preco-preco*40/100),2)
			print(v)
		else:		
			v= round((preco-preco*40/100)+preco*(2/100),2)
			print(v)