x=float(input("alor da comissao"))

if(x>1000):
	y=(1000*0.05)+(x-1000)*0.10
else:
	y=x*0.05
print(round(y,2))
