from numpy import*
vnp = array(eval(input("Nomes dos produtos:")))
vqp = array(eval(input("Quantidade de produtos:")))

v = ("ARROZ", "FEIJAO", "BIS", "MIOJO", "FANTA")
u = (1.25,2.60,1.80,0.85,3.20)

c = 0
soma = 0

while(c<size(vnp)):
	if(vnp[c]==v[0]):
		soma += u[0]*vqp[c]
	elif(vnp[c]==v[1]):
		soma += u[1]*vqp[c]
	elif(vnp[c]==v[2]):
		soma += u[2]*vqp[c]
	elif(vnp[c]==v[3]):
		soma += u[3]*vqp[c]
	elif(vnp[c]==v[4]):
		soma += u[4]*vqp[c]
	c += 1
print(round(soma,2))

