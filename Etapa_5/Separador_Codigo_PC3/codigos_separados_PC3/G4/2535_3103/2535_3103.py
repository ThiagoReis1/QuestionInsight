DA = float(input('Qual o valor depositado no banco A?: '))
DB = float(input('Qual o valor depositado no banco B?: '))
JA = float(input("Qual a taxa de juros do banco A?: "))
JB = float(input("Qual a taxa de juros do banco B?: "))
JA = JA / 100
JB = JB / 100
mes = 0
if(DA > 0 and DB > 0 and JA > 0 and DA > DB and JA < JB):
	while(DB < DA):
		DA = round((DA + (DA * JA)),2)
		DB = round((DB + (DB * JB)),2)
		mes = mes + 1
	print(mes)	
else:
	print("Dados incorretos")
		
