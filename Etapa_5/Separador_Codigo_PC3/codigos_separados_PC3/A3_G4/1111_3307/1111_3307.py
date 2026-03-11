# 	UNIVERSIDADE FEDERAL DO AMAZONAS
# NATÁLIA DE SOUSA RUFINO

# Caso 1
nhe = float(input('Numero de horas extras de F: '))
nhf = float(input('Numero de horas nao trabalhadas de F: '))
nhe = round(nhe, 2)
nhf = round(nhf, 1)
print('Entradas:', nhe, 'horas extras e', nhf, 'horas de falta')

# Indice H
H = nhe - ((2 / 3) * nhf)
# Faixas de H
f1 = 600
f2 = 1200
f3 = 1800
f4 = 2400

if nhe > 0 and nhf > 0:
	if H <= 600:
		print('Gratificacao: R$ 100.0')
	elif H <= 1200:
		print('Gratificacao: R$ 200.0')
	elif H <= f3:
		print('Gratificacao: R$ 300.0')
	elif H <= f4:
		print('Gratificacao: R$ 400.0')
	else:
		print('Gratificacao: R$ 500.0')
else: 
	print('Dados invalidos')
		


