import numpy
def lista(xs,ys):
	retorno=0
	k=0
	for x in xs:
		retorno=retorno+x-ys[k]
		k=k+1
	return retorno
xs=numpy.array(eval(input()))
ys=numpy.array(eval(input()))
print(lista(xs,ys))