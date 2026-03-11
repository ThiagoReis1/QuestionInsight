from numpy import*
from numpy.linalg import*

tempos=array(eval(input("Digite os tempos dos banhos: ")))
percentual=array(eval(input("Digite os percentuais de abertura da torneira: ")))

a=0

for i in range(size(tempos)):
	a=a+(5*percentual[i]*tempos[i]/100)

print(a)


