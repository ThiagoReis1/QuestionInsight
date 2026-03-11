E=float(input("qual o numero de horas extras trabalhadas? "))
F=float(input("qual o numero de horas nao trabalhadas? "))
H = E-(2/3*F)
if(H>2400):
	print("Entradas:",E,"horas extras e",F,"horas de falta")
	print("Gratificacao: R$ 500.00")
elif(H>1800 and H<=2400):
	print("Entradas:",E,"horas extras e",F,"horas de falta")
	print("Gratificacao: R$ 400.00")
elif(H>1200 and H<=1800):
	print("Entradas:",E,"horas extras e",F,"horas de falta")
	print("Gratificacao: R$ 300.00")
elif(H>600 and H<=1200):
	print("Entradas:",E,"horas extras e",F,"horas de falta")
	print("Gratificacao: R$ 200.00")
elif(H<=600 and H>=0):
	print("Entradas:",E,"horas extras e",F,"horas de falta")
	print("Gratificacao: R$ 100.00")
else:
	print("Entradas:",E,"horas extras e",F,"horas de falta")
	print("Dados invalidos")