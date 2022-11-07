# Faça um programa que receba o nome da pessoa, e o salário liquido dessa pessoa, e pergunte se tem outra fonte de receita, se sim adiciona o valor ao salário.
#Depois calcule as despesas com agua, luz, internet, faculdade, cartao de credito, lazer, alimentação e academia. Ao final mostre quanto restou o se está no cheque especial com saldo negativo.
#Caso o saldo positivo pergunte se a pessoa deseja aplicar o dinheiro rendendo 1% ao mês, ela terá o saldo ao final de um mês com o juros acrescido e exiba o valor. Por fim pergunte se deseja fazer
#um calculo de outra pessoa e repetir a operação.

quer = "sim"
while quer == "sim":
    nome = str(input("Qual seu nome? "))
    salarioliquido = float(input("Quanto você recebe? "))

    print("você tem alguma fonte de renda extra? Se sim anote o valor abaixo")

    renda = float(input("renda extra: "))

    salariototal = salarioliquido + renda
    print("O seu sálario total mensal é:", salariototal)

    agua = float(input("Qual o valor da sua conta de água? "))
    luz = float(input("Qual o valor da sua conta de luz? "))
    internet = float(input("Qual o valor da sua conta de internet? "))
    faculdade = float(input("Quanto você paga de faculdade? "))
    cartao = float(input("Quanto você paga de cartão de crédito? "))
    lazer = float(input("Quanto você gasta em lazer? "))
    alimentacao = float(input("Quanto você paga em alimentação? "))
    academia = float(input("Quanto você gasta em academia? "))

    restou = salariototal - agua - lazer - luz - internet - faculdade - cartao - academia - alimentacao


    if (restou <=0):
        print("Seu saldo está em negativo:", restou)
    elif (restou >=1):
        print("Restou do seu sálario:", restou)

    if (restou >1):
       deseja = str(input("seu saldo foi positivo deseja colocar esse dinheiro para render 1%? "))
       match (deseja):
        case ("sim"):
            print("Esse dinheiro renderá no final no mêS", restou*1/100, "reais")
        case ("não"):
            print("okay, tenha um bom mês!")

    quer = input("Quer fazer essa conta para outra pessoa? ")






