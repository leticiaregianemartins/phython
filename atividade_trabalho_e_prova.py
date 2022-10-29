# Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho. Após deverá mostrar na tela a média obtida no 1º, 2º, 3º e 4º
# bimestre.
# • E depois o total informado se o aluno foi aprovado, esta em
# recuperação ou foi reprovado sem recuperação.

prova1 = float(input("digite o resultado da 1 prova: "))
prova2 = float(input("digite o resultado da 2 prova: "))
prova3 = float(input("digite o resultado da 3 prova: "))
prova4 = float(input("digite o resultado da 4 prova: "))
trabalho1 = float(input("digite o resultado da 1 trabalho: "))
trabalho2 = float(input("digite o resultado da 2 trabalho: "))
trabalho3 = float(input("digite o resultado da 3 trabalho: "))
trabalho4 = float(input("digite o resultado da 4 trabalho: "))

b1 = float(prova1 + trabalho1)
b2 = float(prova2 + trabalho2)
b3 = float(prova3 + trabalho3)
b4 = float(prova4 + trabalho4)

b1 = float(b1 / 2)
print("media 1° Bimestre", b1)
b2 = float(b2 / 2)
print("media 2° Bimestre", b2)
b3 = float(b3 / 2)
print("media 3° Bimestre", b3)
b4 = float(b4 / 2)
print("media 4° Bimestre", b4)

resultado = b1 + b2 + b3 + b4
if(resultado >= 60 and resultado <= 100):
    print("você foi aprovado")
elif(resultado >=40 and  resultado <60):
    print("você está de recuperação")
elif(resultado >=0 and resultado <=40):
    print("você está reprovado")
