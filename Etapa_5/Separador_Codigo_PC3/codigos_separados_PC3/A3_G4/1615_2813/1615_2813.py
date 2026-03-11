from numpy import*
v1 = array(eval(input("primeiro: ")))
v2 = array(eval(input("segundo: ")))

i = 0
c = 0
t = 0
b = 0

while(i <size(v1)):
	if(v1[i]== 1):
		t = t + 40
	if(v1[i] == 2):
		t = t + 20
	if(v1[i] == 3):
		t = t + 10
	if(v1[i] >= 4):
		t = t + 0
	i = i+1
print(t)		
while(c <size(v2)):
	if(v2[c]== 1):
		t = t + 40
	if(v2[c] == 2):
		t = t + 20
	if(v2[c] == 3):
		t = t + 10
	if(v2[c] >= 4):
		t = t + 0
	c = c+1

if(v1<v2):
	print("JOGADOR UM")
if(v2>v1):
	print("JOGADOR DOIS")
if(v2 == v1):
	print("EMPATE")
