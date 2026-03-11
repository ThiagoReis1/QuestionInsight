pc = float(input())

if(pc <= 50):
	vf = pc + pc*(100/100)
elif(pc > 50 and pc <=100):
	vf = pc  + pc*(50/100)
elif(pc > 100 and pc <= 500):
	vf = pc + pc*(40/100)
else: 
	vf = pc + pc*(30/100)

print(round(vf,2))