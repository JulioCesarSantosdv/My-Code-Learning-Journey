"""
Elaborar um programa que apresente o valor da conversão em real (R$) de um
valor lido em dólar (US$).O programa deve solicitar o valor da cotação do dólar
e também a quantidade de dólares disponível com o usuário.
==============================================================================
Entendimento:
1.Ler o valor de Dólar em números reais(d)
2.Ler o valor de cotação em números reais(c)
3.Calcular a conversão de dólar em reais
4.Escreva R
"""
d = float(input('Informe um valor em dólar:  '))
c = float(input('Informe o valor de cotação: '))
r = (d*c)
print(f'Com dólar cotado a R${c:.2f} , US${d:.2f}  vale R${r:.2f}.')
