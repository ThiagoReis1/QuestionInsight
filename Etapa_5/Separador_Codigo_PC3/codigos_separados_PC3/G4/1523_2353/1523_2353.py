qi=int(input("digite a quantidade inicial: "))
qc=int(input("digite a quatidade de baloes: "))
qd=int(input("digite a quantidade de baloes: "))

soma=qi
t=0


while(soma<200):
	
	soma=soma+(qc-qd)
	t=t+1

print(t)