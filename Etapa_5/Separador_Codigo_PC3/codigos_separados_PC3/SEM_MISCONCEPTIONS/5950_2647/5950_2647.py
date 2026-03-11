tipo = input()
qtipo = int(input())
qcapu = int(input())

if(tipo.upper()=='T'):
	print(round(qtipo*6.00+qcapu*4.50,2))

if(tipo.upper()=='P'):
	print(round(qtipo*5.00+qcapu*4.50,2))
