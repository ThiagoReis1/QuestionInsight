Q0=1500
t=36
j=float(input("Taxa de juros aplicada:"))
vf=int(input("Valor do apartamento:"))
Qf=Q0*(1+j)**t
print(round(Qf, 2))
if  (Qf>=vf):
	  mensagem="Sim"
else: 
	  mensagem="Nao"
print(mensagem)