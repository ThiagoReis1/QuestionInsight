from numpy import*

r = array(eval(input("Infome a pontuacao: ")))
i = 0
pj = 0

while(i < len(r)):
	if(r[i] == '1'):
		pj = r * 2
	elif(r[i] == '2'):
		pj = r
	elif(r[i] == '3'):
		pj = r // 2
	elif(r[i] == '4'):
		pj = r // 4
	i = i + 1
print(round(pj,2))