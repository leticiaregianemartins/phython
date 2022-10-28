# Crie um programa para realizar as operações de uma tabuada de multiplicação, onde será solicitado ao usuário digitar qual
# numero será a tabuada e qual intervalo do inicio e fim da
# tabuada, e exibir na tela o resultado conforme intervalo.
# • Repetição usando “PARA”
# for i in n:
# for i in range(10):

numero = int(input("digite um número inteiro"))
inicio = int(input("digite o inicio da tabuada"))
fim = int(input("digite o fim da tabuada"))
a = 1
fim = fim +1
if (fim < inicio):
    a = -1
    fim = fim-2
for i in range(inicio,fim, a):
    resultado = numero * i
    print("o resultado dá multiplicação " + str(numero) + " * " + str(i) + " é : " + str(resultado))

