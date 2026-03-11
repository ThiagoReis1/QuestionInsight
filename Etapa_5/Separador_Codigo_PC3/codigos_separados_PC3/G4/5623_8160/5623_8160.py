x= str(input('bolo ou salgado(B/S): ')).upper()
q1= int(input('quantidade de bolo ou salgado: '))
q2= int(input('quantidade de cappucino'))
b= q1*5 + q2*7.50
s= q1*4 + q2*7.50
if(x== 'B'):
	print(b)
else:
	print(s)