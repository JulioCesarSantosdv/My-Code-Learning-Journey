"""
Elaborar um programa que apresente o valor da conversão em euros (€) de
um valor lido em real (R$).O programa deve solicitar o valor da cotação
do euro e também a quantidade de reais disponível com o usuário.
========================================================================
Entendimento:
1.Ler um valor em reais em números reais (r)
2.Ler o valor de contação em números reais(c)
3.Calcular e = r/c
4.Escreva d
"""
r = float(input('Informe o valor em reais: '))
c = float(input('Informe o valor de cotação: '))
e = (r/c)
print(f'Com o euro a R${c:.2f}, você com R${r:.2f} pode comprar €{e:.2f}.')