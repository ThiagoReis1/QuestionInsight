L_S = input("lanche ou salgado:").upper()
quan = int(input("quantidade:"))
quan_re = int(input("refrigerante:"))
if(L_S=="L"):
	msg = (5*quan) + (4*quan_re)
else:
	msg = (3.5*quan) + (4*quan_re)
print(float(round(msg,2)))