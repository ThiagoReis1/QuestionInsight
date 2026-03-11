from numpy import*
e = str(input("Quais os estados?: "))
e = e.split(",")
x =  zeros(5,dtype = int)
pam = 0
ppe = 0
pmg = 0
psp = 0
prs = 0
for i in e:
	if(i == "AM"):
		pam = pam + 1
	elif(i == "PE"):
		ppe = ppe + 1
	elif(i == "MG"):
		pmg = pmg + 1
	elif(i == "SP"):
		psp = psp + 1
	elif(i == "RS"):
		prs = prs + 1	
x[0] = pam
x[1] = ppe
x[2] = pmg
x[3] = psp
x[4] = prs
print(max(x))
print(x)