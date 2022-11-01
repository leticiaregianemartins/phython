# Numa fazenda em um local reservado para criação coloca-se um casal de coelhos.
# Supondo que em cada mês, a partir do segundo mês de vida, cada casal dá origem a um novo casal de coelhos, ao fim de um ano, quantos casais de coelhos estão no pátio?
# Escreva um programa para calcular a quantidade de coelhos em um ano.

def coelho(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return coelho(n - 1) + coelho(n - 2)
n = 12
print("terá casais de", coelho(n), "coelho")
