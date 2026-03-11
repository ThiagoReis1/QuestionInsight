from numpy import*
g = array(eval(input("Digite: ")))
for i in  range (size(g)):
	if (g[i] == 0):
		g[i] = 9**3
	elif (g[i] == 1):
		g[i] = 0**3
	elif (g[i] == 2):
		g[i] = 1**3
	elif (g[i] == 3):
		g[i] = 2**3
	elif (g[i] == 4):
		g[i] = 3**3
	elif (g[i] == 5):
		g[i] = 4**3
	elif (g[i] == 6):
		g[i] = 5**3
	elif(g[i] == 7):
		g[i] = 6**3
	elif(g[i] == 8):
		g[i] = 7**3
	elif(g[i] == 9):
		g[i] = 8**3
print(g)