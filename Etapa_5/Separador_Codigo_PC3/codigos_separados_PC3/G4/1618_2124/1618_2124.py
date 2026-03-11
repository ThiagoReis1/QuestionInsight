from numpy import*
v=array(eval(input("Digite um numero:")))

i = 0
j = size(v)-1

k = ""
while(size(v)>0):
	i=i+1
	k= k + str(v[0]) + "x^" + str(j)

	print(k)