from numpy import*
m = array(eval(input().upper()))
n = array(eval(input()))

j = 0
dm = 0
while (j < size(n)):
	if (m[j] == "GELO"):
		dm = dm + n[j]*2
	elif (m[j] == "FOGO"):
		dm = dm + n[j]*3
	elif (m[j] == "CHOQUE"):
		dm = dm + n[j]*4
	elif (m[j] == "CONJURACAO"):
		dm = dm + n[j]*8
	elif (m[j] == "ILUSAO"):
		dm = dm + n[j]*10
	j = j + 1

print(int(dm))