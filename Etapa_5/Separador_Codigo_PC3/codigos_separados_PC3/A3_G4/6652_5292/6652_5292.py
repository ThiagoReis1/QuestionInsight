from numpy import*

notas = array(eval(input("digite as notas : ")))
peso = array([2,2,6,1])

num = 0
den = sum(peso)

num = (peso[0] * notas[0] )+ (peso[1]*notas[1]) + (peso[2]*notas[2])+(peso[3]*notas[3])


print(round(num/den, 2))


	
	