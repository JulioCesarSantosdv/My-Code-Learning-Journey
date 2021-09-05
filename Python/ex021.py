"""
Elabore um programa que calcule  e apresente o valor do volume de uma
lata de óleo,utilizando a fórmula VOLUME = 3.14159*RAIO**2*ALTURA.
=================================================================================
Entendimento
1. Fazer a leitura de RAIO e ALTURA como números reais.
2. Calcular VOLUME conforme a fórmula
3. Escrever VOLUME
"""
RAIO = float(input('Informe o valor do raio: '))
ALTURA = float(input('Informe o valor da ALTURA: '))
VOLUME = 3.14159*RAIO**2*ALTURA
print(f'O valor do volume é de {VOLUME:.2f}.')
print('FIM')


