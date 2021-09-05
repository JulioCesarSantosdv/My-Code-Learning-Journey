"""
Elaborar um programa que apresente o valor da conversão em dólar (US$) de
um valor lido em real (R$).O programa deve solicitar o valor da cotação
do dólar e também a quantidade de reais disponível com o usuário.
========================================================================
Entendimento:
1.Ler um valor em reais em números reais (r)
2.Ler o valor de contação em números reais(c)
3.Calcular d = r/c
4.Escreva d
"""
r = float(input('Informe o valor em reais: '))
c = float(input('Informe o valor de cotação: '))
d = (r/c)
print(f'Com o dólar a R${c:.2f} você com R${r:.2f} pode comprar US${d:.2f}.')