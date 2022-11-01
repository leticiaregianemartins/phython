# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, mostre todos os descontos, mostre o salário bruto e o líquido.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# • Salário Bruto : R$ - IR (11%) : R$ - INSS (8%) : R$ - Sindicato ( 5%)
# • Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

trabalha = float(input("Quanto você ganha por hora? "))
hora = float(input("Quantas horas você trabalha? "))

pordia = trabalha * hora

mes = pordia * 30
print("O seu sálario liquido é", mes)

bruto = mes * 8 / 100 and mes * 11 / 100 and mes * 5 / 100
print("será descontado do seu sálario", bruto )

bruto2 = mes - bruto
print("O seu sálario bruto é", bruto2)