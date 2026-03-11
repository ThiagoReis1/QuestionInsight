from numpy import*

v = array(eval(input()))
n = array(eval(input()))
v1= int(v[0]*40 + v[1]*20 + v[2]*10+ v[3]*0)
n1= int(v[0]*40 + v[1]*20 + v[2]*10+ v[3]*0)

if v1>n1:
	print("JOGADOR DOIS")
elif n1>v1:
   print("JOGADOR UM")
else:
	print("EMPATE")
