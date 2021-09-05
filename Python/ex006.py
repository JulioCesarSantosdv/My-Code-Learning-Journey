"""
Desenvolva um programa que efetue o cálculo e apresente o valor de uma prestação
de um bem em atraso, utilizando a fórmula PRESTAÇÃO=VALOR+(VALOR*(TAXA/100)*TEMPO).
================================================================================
Entendimento:
1.Fazer a leitura de valor e taxa como números reais
2.Fazer a leitura de tempo como número inteiro.
3.Calcular a prestação conforme a fórmula.
4.Escreva prestação
"""
VALOR = float(input('Informe o valor em R$: '))
TAXA = float(input('Informe a taxa : '))
TEMPO = int(input('Informe o tempo: '))
PRESTACAO = VALOR+(VALOR*(TAXA/100)*TEMPO)
print(PRESTACAO)
print('FIM')
