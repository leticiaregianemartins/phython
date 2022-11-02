# Crie um programa que leia um conjunto de nomes de 20 estudantes
# inscritos na prova do ENEM. Com esses nomes, realizar uma
# ordenação crescente usando uma função para facilitar a localização
# do nome na lista que será afixada no quadro de avisos da escola.
# def nomeDaFuncao():
# #linhas de comando da função
# #Se tiver parâmetros é só colocar no parênteses (parm1, param2)
# Para chamar a função é
# nomeDaFuncao()
# #se tiver que passar parâmetros é só colocar no parêntese (param1, param2)

lista_nomes_enem = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



for i in range(20):
    lista_nomes_enem[i] = str(input("digites os nomes dos estudantes "))

lista_nomes_enem.sort()
print(lista_nomes_enem)



