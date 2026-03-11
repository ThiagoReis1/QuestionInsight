lam=int(input("Informe população inicial de lambaris:"))
tuc=int(input("Informe população inicial de tucunares: "))
txlam=float(input("Informe taxa de crescimento de lambaris:"))
txtuc=float(input("Informe taxa de crescimento de tucunares:"))
t=1
i=0
while(lam<=tuc):
	lam=(lam*txlam)-2
	tuc=(tuc*txtuc)
	novalam=lam
	i=i+1
	t=t+1
print(t)