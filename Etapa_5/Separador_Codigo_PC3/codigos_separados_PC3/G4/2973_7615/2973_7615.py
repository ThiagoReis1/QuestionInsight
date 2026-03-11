s0 = int(input("posicao inicial:"))
v= int(input("velocidade do objeto:"))
t= int(input("tempo de deslocamento:"))

s= (s0 + (v*t))
l= 100

if (v <= l):
	m= "OK"
else:
	m= "ACIMA"
	
print (s)
print (m)