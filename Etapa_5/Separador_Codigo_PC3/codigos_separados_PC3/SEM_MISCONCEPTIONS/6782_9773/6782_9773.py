num=int(input())
pais=input()
pais=pais.upper()
idade=2023-num
if pais=='B':
	idademinima=18
	if idade >=idademinima:
		print("sim")
		print(idademinima-idade)
	else:
		print("nao")
		print(idademinima%idade)
elif pais=='E':
	idademinima=16
	if idade>=idademinima:
		print("sim")
		print(idademinima-idade)
	else:
		print("nao")
		print(idademinima%idade)
else:
	print("invalido")
		