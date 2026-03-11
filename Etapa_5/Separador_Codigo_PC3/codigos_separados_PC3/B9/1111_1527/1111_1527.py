#UFAM - Universidade Federal do Amazonas
#Laís Amorim Reis - 21602327

horas_extras = float(input("Número de horas extras: "))
horas_nao_trabalhadas = float(input("Número de horas não trabalhadas: "))

print("Entradas: ",horas_extras," horas extras e ",horas_nao_trabalhadas," horas de falta")

H = (horas_extras) - ((2*horas_nao_trabalhadas)/3)

if(horas_extras < 0 or horas_nao_trabalhadas < 0):
	print("Dados invalidos")
	
elif(H>2400):
	print("Gratificacao: R$ 500.0")
elif(H>1800 and H<=2400):
	print("Gratificacao: R$ 400.0")
elif(H>1200 and H<=1800):
	print("Gratificacao: R$ 300.0")
elif(H>600 and H<=1200):
	print("Gratificacao: R$ 200.0")
else:
	print("Gratificacao: R$ 100.0")
	
	