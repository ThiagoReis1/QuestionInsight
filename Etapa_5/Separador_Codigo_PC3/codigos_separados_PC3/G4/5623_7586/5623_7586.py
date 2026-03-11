tipo = input("bolo ou salgado: ").upper()
qa= int(input("quantidade de fatias: "))
qb= int(input("quantidade de cappuccinos: "))

if tipo == "B":
	
	conta = (qa * 5)+(qb * 7.50)
	print(conta)
	
else: 
	
	conta =(qa * 4)+(qb * 7.50)
	print(conta)