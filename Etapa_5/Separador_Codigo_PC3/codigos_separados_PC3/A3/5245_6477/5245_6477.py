sal_at = float(input("Digite o salario: "))

print("Entrada: R$", sal_at)
novo_sal=-1
if (sal_at >0) and(sal_at <= 800):
	novo_sal = sal_at + sal_at * 0.5

elif ((sal_at > 800) and (sal_at <= 1000)):
	novo_sal = sal_at + sal_at * 0.4

	
elif (sal_at > 1000) and (sal_at <= 1200):
	novo_sal = sal_at +sal_at * 0.3

elif (sal_at > 1200) and (sal_at <= 1400):
	novo_sal = sal_at + sal_at * 0.2


elif (sal_at > 1400) and (sal_at <= 1600):
	novo_sal = sal_at + sal_at * 0.1

elif (sal_at > 1600):
	novo_sal = sal_at + sal_at * 0.05
	
else:
	print("Dado invalido")
if novo_sal != -1 :	
   print("Novo salario: R$", round(novo_sal, 2))