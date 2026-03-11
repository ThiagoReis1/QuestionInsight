nome = input("").lower()
C = 12.011
H = 1.0079
O = 15.9994
S = 32.066
N = 14.0067
SF = (9*C + 11*H + 2*O + S)
ST = (9*C+ 11*H+ N+O*3)

if(nome == "fenilalanina"):
	SF = (9*C + 11*H + 2*O + S)
	print(round(SF, 2))
else:
	print(round(ST, 2))
	
	