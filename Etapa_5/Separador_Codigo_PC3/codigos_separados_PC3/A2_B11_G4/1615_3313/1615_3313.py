from numpy import*
v1 = array(eval(input("insira os acertos: ")))
v2 = array(eval(input("insira os acertos: ")))
i = 0
jog1 = 0
jog2 = 0
while(i<size(v1)):
	if(v1[i]==1):
		jog1 = jog1 + 40
	if(v1[i]==2):
		jog1 = jog1 + 20
	if(v1[i]==3):
		jog1 = jog1 + 10
	if(v1[i]==4):
		jog1 = jog1 
	if(v2[i]==1):
		jog2 = jog2 + 40
	if(v2[i]==2):
		jog2 = jog2 + 20
	if(v2[i]==3):
		jog2 = jog2 + 20
	if(v2[i]==4):
		jog2 = jog2 
	i = i+1
if(jog1>jog2):
	print("JOGADOR UM")
if(jog2>jog1):
	print("JOGADOR DOIS")
if(jog1 == jog2):
	print("EMPATE")