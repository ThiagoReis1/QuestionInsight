# Universidade Federal do Amazonas
# Aluno: Nelson Geraldo A. de Carvalho
# Curso: Estatistica

autorizado = None
mais_alto = None

# Inputs
sua_altura = float(input('Digite sua altura em metros: '))
amigo_altura = float(input('Digite a altura do seu amigo (em metros): '))


# Calculo
if (sua_altura == 1.37 or amigo_altura == 1.37):
	autorizado = 'Sim'
elif (sua_altura > 1.37 or amigo_altura > 1.37):
	autorizado = 'Sim'
else:
	autorizado = 'Nao'

if (sua_altura > amigo_altura):
	mais_alto = sua_altura
else:
	mais_alto = amigo_altura

# Outputs
print(autorizado)
print(mais_alto)