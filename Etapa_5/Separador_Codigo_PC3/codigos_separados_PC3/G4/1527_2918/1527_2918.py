f = int (input ("insira a quantidade de seguidores de Forseti: "))
l = int (input ("insira a quantidade de seguidores de Loki: "))
pf = float (input ("insira o percentual anual de crescimento de seguidores de Forseti: "))
pl = float (input ("insira o percentual anual de crescimento de seguidores de Loki: "))
t = 0
while (l <= f):
	l = l + (l * pl / 100)
	f = f + (f * pf / 100)	
	t = t + 1
print (t)