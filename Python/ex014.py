"""
Elaborar um programa que apresente o valor da conversão em real (R$) de um
valor lido em euros (€).O programa deve solicitar o valor da cotação do euro
e também a quantidade de euros disponível com o usuário.
==============================================================================
Entendimento:
1.Ler o valor de euros em números reais(e)
2.Ler o valor de cotação em números reais(c)
3.Calcular a conversão de euros em reais
4.Escreva R
"""
e = float(input('Informe um valor em euros:  '))
c = float(input('Informe o valor de cotação: '))
r = (e*c)
print(f'Com euro cotado a R${c:.2f} , €{e:.2f}  vale R${r:.2f}.')
