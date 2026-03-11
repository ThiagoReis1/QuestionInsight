import math
sal = float(input("Digite o valor do seu salario: " ));
if(sal > 0):
	if(sal <= 800.00):
		nsal = sal + sal * (50 / 100);
		print("Entrada:", "R$", sal)
		print("Novo salario:", "R$", round(nsal,2));
	elif(sal > 800.00 and sal <= 1000.00):
		nsal = sal + sal * ( 40 / 100);
		print("Entrada:", "R$", sal)
		print("Novo salario:", "R$", round(nsal,2));
	elif(sal > 1000.00 and sal <= 1200.00):
		nsal = sal + sal * ( 30 / 100);
		print("Entrada:", "R$", sal)
		print("Novo salario:", "R$", round(nsal,2));
	elif(sal > 1200.00 and sal <= 1400.00):
		nsal = sal + sal * ( 20 / 100);
		print("Entrada:", "R$", sal);
		print("Novo salario:", "R$", round(nsal,2));
	elif(sal > 1400.00 and sal <= 1600.00):
		nsal = sal + sal * ( 10 / 100);
		print("Entrada:", "R$", sal);
		print("Novo salario:", "R$", round(nsal,2));
	elif(sal > 1600.00):
		nsal = sal + sal * ( 5 / 100);
		print("Entrada:", "R$", sal);
		print("Novo salario:", "R$", round(nsal,2));
else:
	print("Entrada:", "R$", sal);
	print("Dado invalido")
	