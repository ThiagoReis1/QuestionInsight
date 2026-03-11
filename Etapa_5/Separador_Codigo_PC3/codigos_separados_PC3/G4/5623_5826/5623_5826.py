lanche = input("Digite qual o seu lanche: ").upper()
q1= int(input("Digite a quantidade de fatias de bolo ou salgado: "))
q2 = int(input("Digite a quantidade de cappuccinos: "))

if(lanche == "B"):
	t = 5*q1 + 7.5*q2
	print(round(t,2))
if(lanche == "S"):
	t1 = 4*q1 + 7.5*q2
	print(round(t1,2))