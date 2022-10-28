# Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na tela se o aluno foi aprovado, se está em recuperação ou foi reprovado
# sem chance de recuperação.
# embrando que cada bimestre vale 25 pontos num total anual de 100 pontos.

print("lançamento de notas")
b1 = float(input("digite a nota do primeiro bimestre: "))
b2 = float(input("digite a nota do segundo bimestre: "))
b3 = float(input("digite a nota do terceiro bimestre: "))
b4 = float(input("digite a nota do quarto bimestre: "))

notatotal = float(b1 + b2 + b3 + b4)
if(notatotal >= 60 and notatotal <= 100):
    print("você foi aprovado")
elif(notatotal >=40 and  notatotal <60):
    print("você está de recuperação")
elif(notatotal >=0 and notatotal <=40):
    print("você está reprovado")

