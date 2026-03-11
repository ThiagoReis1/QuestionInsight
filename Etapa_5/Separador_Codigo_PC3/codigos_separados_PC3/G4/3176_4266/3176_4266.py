from numpy import*

s = input("Digite uma palavra: ")
t=0
vg=0
con=0
for i in s:
	if (s[t]=="a") or (s[t]=="e") or (s[t]=="i") or (s[t]=="o") or (s[t]=="u"):
		vg = vg+1
	else:
		con = con+1
	t=t+1
print(vg)
print(con)