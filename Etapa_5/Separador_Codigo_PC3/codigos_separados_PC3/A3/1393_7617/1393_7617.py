# Universidade Federal do Amazonas
# Aluno: Nelson Geraldo A. de Carvalho
# Curso: Estatistica

# SE encomenda < 5000g, cobrado 0.05 por grama
# SE encomenda >= 5000g, cobrado 0.04 por grama, + 60.00

valor_total = 0;

# Inputs
peso_encomenda = float(input('Digite o peso da encomenda em gramas: '))

# Calculos
if(peso_encomenda < 5000):
	valor_total = peso_encomenda * 0.05
else:
	valor_total = (peso_encomenda * 0.04) + 60.00

# Outputs
valor_frete = valor_total
print(round(valor_frete, 2))
