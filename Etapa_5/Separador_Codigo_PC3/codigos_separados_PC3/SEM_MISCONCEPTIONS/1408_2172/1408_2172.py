nome_da_arma=input("digiteo o nome da arma:(katana/sabre)")
destreza=int(input("digite a destreza:"))
vlr1=int(input("digite o valor sorteado:"))
vlr2=int(input("digite o outro valor sorteado:"))

S=vlr1+vlr2


if(nome_da_arma=="katana"):
	dano=2*S+destreza
	print(dano)
else:
	dano=S+2*destreza
	print(dano)