# lojavirtual

iphone = 2980
samsung = 2540
tablet = 1950
ps5 = 2100
notebook = 2350

quantidade1 = int(input("quantos iphone você quer comprar?"))
quantidade2 = int(input("quantos samsung você quer comprar?"))
quantidade3 = int(input("quantos tablet você quer comprar?"))
quantidade4 = int(input("quantos PS5 você quer comprar?"))
quantidade5 = int(input("quantos notebook você quer comprar?"))

valor = (quantidade1 * iphone) + (quantidade2 * samsung) + (quantidade3 * tablet) + (quantidade4 * ps5) + (quantidade5 * notebook)
print("O valor total da compra é", valor)

valor2 = valor/3
print("A parcela ficará", valor2)

valor2 = ((valor*5/100) + valor)/6
print("A parcela com o acréscimo de 5% ficará", valor2)

valor2 = ((valor*10/100) - valor)
print("O valor com desconto de 10% é", valor2)