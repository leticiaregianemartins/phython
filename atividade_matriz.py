# Crie um programa em que o usuário deve digitar números
# inteiros para uma matriz de 5 linhas e 5 colunas .
# • Após a digitação dos números, o usuário deve digitar um número aleatório e verificar se ele se encontra na matriz.
# • Ao final, os índices da linha e da coluna devem ser impressos se o elemento for encontrado;
# caso contrário, a mensagem “elemento não encontrado” deve ser mostrada na tela.

lista = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i in range(5):
    for j in range(5):
        lista[i][j] = int(input("digite um número inteiro "))

n1 = int(input("digite um número para localizar na matriz "))
encontrado = False

for i in range(5):
    for j in range(5):
        if lista[i][j] == n1:
            print("número encontrado", n1, "na posição", lista[i][j])
            encontrado = True
if(encontrado is False):
    print("Não foi encontrado na matriz seu número")

