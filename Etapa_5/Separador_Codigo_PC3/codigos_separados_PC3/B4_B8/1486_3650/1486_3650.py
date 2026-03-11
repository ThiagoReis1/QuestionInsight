receita = input("nome da receita").lower()
quant = float(input('quantidade de ingrediente'))

if((quant>=0)and(quant<=10000)):
   if(receita == 'arroz'):
	   x = int(quant/500)
	   print(x)
   elif(receita == 'cenoura'):
	   x = int(quant/100)
	   print(x)
   elif(receita == 'kampyo'):
	   x = int(quant/20)
	   print(x)
   elif(receita == 'nori'):
	   x = int(quant/50)
	   print(x)
   elif(receita == 'omelete'):
	   x = int(quant/200)
	   print(x)
   elif(receita == 'pepino'):
	   x = int(quant/150)
	   print(x)
   elif(receita == 'salmao'):
	   x = int(quant/300)
	   print(x)
   elif(receita == 'shitake'):
	   x = int(quant/150)
	   print(x)
else:
	print(' Entrada invalida')