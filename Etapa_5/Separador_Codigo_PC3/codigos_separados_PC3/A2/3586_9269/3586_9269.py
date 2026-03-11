from numpy import*
v = array(eval(input(" ")))
i = 0
pontos1 = 0
pontos2 = 0
pontos3 = 0
pontos4 = 0
t1,t2,t3,t4 = 0,0,0,0

while (i < size(v)):
	if (v[i] == 1):
		pontos1 = pontos1 + 100
		t1 = t1 + 1
	if (v[i] == 2):
		pontos2 = pontos2 + 60
		t2 = t2 + 1
	if (v[i] == 3):
		pontos3 = pontos3 + 20
		t3 = t3 + 1
	else:
		pontos4 = pontos4
		t4 = t4 + 1
	i = i + 1
print(pontos1 + pontos2 + pontos3 + pontos4)