t = float(input(''))
qf =1042000
q0 = 1500
i = ((qf/q0)**(1/t))-1
if i <= 0.01 :
	print(round(i,5))
	print('Real')
else:
	print(round(i,5))
	print('Irreal')