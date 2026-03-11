tapioca = 3.50
salgado = 5
acai = 13

com = (input("digite:"))
qntdet = float(input("digite:"))            
qntdea = float(input("digite"))

if com == 'T':
	conta = float(tapioca*qntdet)+(acai*qntdea)
	print(conta)
else:
	conta = float(salgado*qntdet)+(acai*qntdea)
	print(conta)