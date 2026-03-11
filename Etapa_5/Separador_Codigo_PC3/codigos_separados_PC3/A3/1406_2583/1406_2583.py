golpe = input()
N = int(input())
t = int(input())
cuspe = 2 * N
cauda = N
if(golpe == "cauda"):
	vida = N * t 
else:
	vida = 2 * N * t
	
print(vida)