vtprazo = float(input())
qpmensal = float(input())
taxames = 3

juros = (vtprazo * taxames * qpmensal) / 100

m = vtprazo + juros

print(round(m, 2))
