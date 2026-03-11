A= float(input(""))
T = float(input(""))
ac = 1.65
tc = 0.02
anos = 0
while(ac>A):
	A = A + T
	ac = ac + tc
	anos = anos + 1
print(anos)