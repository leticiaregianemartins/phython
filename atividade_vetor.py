# Faça um Programa que leia em um vetor de 10 caracteres (letras ) e diga quantas consoantes foram lidas.
# Mostre as consoantes

lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1, 10):
    lista[i] =str(input("digite uma letra para a matriz "))

letra = str(input("digite uma consoante para localizar na matriz "))
encontrado = False


for i in range(1, 10):
    if lista[i] == letra:
        print("A letra encontrada", letra)
        encontrado = True

if encontrado is False:
    print("Não tem essa consoante")

for i in range(1, 10):
    if lista[i] != "a" and lista[i] != "e" and lista[i] != "i" and lista[i] != "o" and lista[i] != "u":
        print(lista[i])

