p= input('T para tapioca, ou S para salgado: ')
if p == 'S': 
	s= int(input("quantidade de salgados?"))
	a= int(input("quantidade de acai?"))
	print(round((s*4) + (a*10),2))
else:
	t= int(input("quantidade de tapiocas?"))
	a= int(input("quantidade de acai?"))
	print(round((t*5.5) + (a*10),2))