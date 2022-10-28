# Crie um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = int(input("qual turno você estuda? Coloque 1 se for Manhã, 2 se for Tarde ou 3 se for Noite"))


match (turno):
    case (1):
        print("Bom dia")

    case (2):
        print("Boa tarde")

    case (3):
        print("Boa noite")

# No python, o CASO não é obrigatorio ser número inteiro, ele aceita caractere.
# Se for por só o caractere não colocar o int
# casa_: siginifica caso ao contrario