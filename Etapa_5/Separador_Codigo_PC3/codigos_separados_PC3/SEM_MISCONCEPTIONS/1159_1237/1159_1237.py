Ntambaquis = float(input( "numeroTambaqui: "))

Npacus = float(input( "numeroPacus: "))

TaxaT = float(input("porcentagem em: "))

TaxaP = float(input("porcentagem em: "))

anos = float(input("anos: "))

while (Ntambaquis<Npacus):
	Ntambaquis =  Ntambaquis  * TaxaT/100
	Npacus = Npacus  * TaxaP/100
	anos = anos + 1
	print(anos)
	



