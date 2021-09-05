"""
Desenvolva um programa que calcule o salário líquido de um professor.
Para elaborar o programa,é necessário possuir alguns dados, tais como
valor hora aula,número de horas trabalhadas no mês e percentual de desconto
no INSS. Em primeiro lugar,deve-se estabelecer o seu salário bruto para fazer
o desconto e ter o valor do salário líquido.
===========================================================================
Entendimento:

1.Estabelecer a leitura da variável HT(Horas Trabalhadas no Mês)
2.Estabelecer a leitura da variável VH(Valor Hora Aula)
3.Estabelecer a leitura da variável PD(Percentual de Desconto)
4.Calcular o salário bruto(SB), sendo HT*VH
5.Calcular o total de desconto (TD) com base no valor de PD dividido por 100
6.Calcular o salário líquido(SL),deduzindo o desconto do salário bruto.
7.Apresentar os valores dos salários bruto e líquido: SB e SL
"""
ht =int(input('Digite a quantidade de Horas Trabalhadas no Mês: '))
vh = float(input('Digite o Valor da Hora Aula: '))
pd = float(input('Digite o percentual de desconto: '))
sb = ht*vh
td = (pd/100)*sb
sl = sb - td
print(f'O valor do Salário Bruto é de R${sb} e o salário líquido R${sl}.')
print('FIM')
