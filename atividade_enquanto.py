# Crie um programa de calculadora que realiza as operações de
# soma, multiplicação, divisão e subtração, será perguntado ao
# usuário se deseja continuar com o uso da calculadora, enquanto ele digitar (“S” – Sim) o programa irá reiniciar a calculadora.
# • Repetição usando ”ENQUANTO”
# while == “valor”
# #sendo verdadeiro repete até ser falso

num1 = int(input("digite o primeiro numero"))
num2 = int(input("digite o segundo numero"))
continuar = "sim"

while continuar == "sim":
    resultado = num1 + num2
    print("o resultado é", resultado)

    resultado = num1 - num2
    print("o resultado é", resultado)

    resultado = num1 * num2
    print("o resultado é", resultado)

    resultado = num1 / num2
    print("o resultado é", resultado)

    continuar = input("sim")
    print("deseja continuar", continuar)






