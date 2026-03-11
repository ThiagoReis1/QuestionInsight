N_hb=int(input("Numero de habitantes Bravos: "))
N_hp=int(input("Numero de habitantes Pentos: "))
N_hPr=int(input("Numero de habitantes Porto Real: "))
T_CPB=float(input("Taxa de crescimento populacional de Bravos:"))
T_CPP=float(input("Taxa de crescimento populacional de Pentos:"))
T_CPPR=float(input("Taxa de crescimento populacional de Porto Real:"))


while(N_hb*T_CPB+N_hp*T_CPP > (N_hPr*T_CPPR)):
	N_hb= N_hb*T_CPB
	N_hp= N_hp*T_CPP
	N_hPr= N_hPr*T_CPPR
	anos = anos + 1
print(anos)