from numpy import*
a = array(eval(int(input("digite a mensagem numerica:"))))
x = zeros(size(a),dtype=int)
for i in range(size(x)):
	if a[0] > 0:
		a = (a[i] -1) ** 3
		print(a)
		