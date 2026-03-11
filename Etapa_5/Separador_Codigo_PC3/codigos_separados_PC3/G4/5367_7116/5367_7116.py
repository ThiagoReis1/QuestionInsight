from numpy import*

cpf = array(eval(input(": ")))
vetor_aux = array([1,2,3,4,5,6,7,8,9])
i = 0
acum = 0

while i < 9:
	acum = acum + (cpf[i]*vetor_aux[i])
	i = i + 1
print(acum%11)