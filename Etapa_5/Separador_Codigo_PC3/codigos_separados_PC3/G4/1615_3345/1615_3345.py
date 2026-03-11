from numpy import *
v1 = array(eval(input("Primeiro jogador: ")))
v2 = array(eval(input("Segundo jogador: ")))
i = 0
q1 = 0
q2 = 0
while (i < size(v1)):
	if (v1[i] == 1):
		q1 = q1 + 40
	elif (v1[i] == 2):
		q1 = q1 + 20
	elif (v1[i] == 3):
		q1 = q1 + 10
	else:
		q1 = q1 + 0
	i = i + 1
i = 0
while (i < size(v1)):
	if (v2[i] == 1):
		q2 = q2 + 40
	elif (v2[i] == 2):
		q2 = q2 + 20
	elif (v2[i] == 3):
		q2 = q2 + 10
	else:
		q2 = q2 + 0
	i = i + 1
if (q1 > q2):
	print("JOGADOR UM")
elif (q2 > q1):
	print("JOGADOR DOIS")
else:
	print("EMPATE")