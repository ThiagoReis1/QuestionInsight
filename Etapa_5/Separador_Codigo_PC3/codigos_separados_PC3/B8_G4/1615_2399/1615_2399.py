from numpy import*
j1 = array(eval(input()))
j2 = array(eval(input()))

if(size(j1) == size(j2)):
	if(j1[0] == 1):
		p1 = 40
	elif(j1[0] == 2):
		p1=20
	elif(j1[0] == 3):
		p1=10
	elif(j1[0] >= 4):
		p1=0

	if(j1[1] ==1):
		p2 = 40
	elif(j1[1] == 2):
		p2=20
	elif(j1[1] == 3):
		p2=10
	elif(j1[1] >= 4):
		p2=0

	if(j1[2] == 1):
		p3 = 40
	elif(j1[2] == 2):
		p3=20
	elif(j1[2] == 3):
		p3=10
	elif(j1[2] >= 4):
		p3=0

	if(j1[3] ==1):
		p4 = 40
	elif(j1[3] == 2):
		p4=20
	elif(j1[3] == 3):
		p4=10
	elif(j1[3] >= 4):
		p4=0

	pj1 = p1 + p2 + p3 + p4

	if(j2[0] == 1):
		q1 = 40
	elif(j2[0] == 2):
		q1=20
	elif(j2[0] == 3):
		q1=10
	elif(j2[0] >= 4):
		q1=0

	if(j2[1] == 1):
		q2 = 40
	elif(j2[1] == 2):
		q2=20
	elif(j2[1] == 3):
		q2=10
	elif(j2[1] >= 4):
		q2=0

	if(j2[2] == 1):
		q3 = 40
	elif(j2[2] == 2):
		q3=20
	elif(j2[2] == 3):
		q3=10
	elif(j2[2] >= 4):
		q3=0

	if(j2[3] == 1):
		q4 = 40
	elif(j2[3] == 2):
		q4=20
	elif(j2[3] == 3):
		q4=10
	elif(j2[3] >= 4):
		q4=0

	pj2 = q1 + q2 + q3 + q4

	if(pj1 > pj2):
		print("JOGADOR UM")
	elif(pj2 > pj1):
		print("JOGADOR DOIS")
	else:
		print("EMPATE")
else:
	print("INVALIDOS")