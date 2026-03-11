from numpy import*

vt = array(eval(input("Digite: ")))
v_qt = size(vt)
v_one = ones(v_qt, dtype=int)
v_seq = arange(v_qt,  dtype=int)

peso = v_one + v_seq
dano = v_one * peso
print(dano)