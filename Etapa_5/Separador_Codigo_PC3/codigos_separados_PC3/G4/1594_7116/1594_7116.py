from numpy import*

ag = array(eval(input("ataque do gato: ")))
i = 0
acum = 0
while i < size(ag):
	acum = acum + (ag[i] * (i + 1))
	i = i + 1
print(acum)