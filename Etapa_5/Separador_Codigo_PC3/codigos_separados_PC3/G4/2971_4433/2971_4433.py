j = float(input('taxa de juros:'))
valor_apartamento = float(input('valor:'))

Q0 = 1500
t = 36

Qf = Q0*((1 + j)**t)

if(Qf >= valor_apartamento):
	msg = 'Sim'
else:
	msg = 'Nao'
print(round(Qf, 2))
print(msg)
