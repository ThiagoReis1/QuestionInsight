tempo = int(input())
qf = 1042000.0
q0 = 1500.0

i = ((qf/q0)**(1/tempo)) - 1

print(round(i, 5))

if i <= 0.01:
	print('Real')
else:
	print('Irreal')
