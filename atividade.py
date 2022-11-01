# Faça um programa para imprimir igual abaixo:
# 1
# 2 2
# 3 3 3 ...
# n n n n ...
# “n” para um ”numero” (range) informado pelo usuário.
# • Use uma função que receba um valor n inteiro e imprima até a
# “n-Linha” informada pelo usuário.


n = int(input("Digite : "))

def repeticao(n):
    for i in range(n):
        print(n, end="")

repeticao(n)