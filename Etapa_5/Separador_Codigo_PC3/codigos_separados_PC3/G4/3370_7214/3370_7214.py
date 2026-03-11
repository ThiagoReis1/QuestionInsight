Un = input("Digite a unidade em que a medida esta: ").upper()
Var = float(input("Qual o valor da medida? "))

if (Un == "C"):
	mc = 0.393701*Var

else:
	mc = Var/0.393701
	
print(round(mc,2))