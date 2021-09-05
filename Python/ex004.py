"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus
Celsius.A fórmula de conversão é C = K − 273,15,sendo C a temperatura em
Celsius e K a temperatura em Kelvin .
=============================================================================
Entendimento
1.Fazer a leitura de K como um número real
2.Calcule C mediante a fórmula
3.Escreva C
"""
K = float(input('Informe uma temperatura em K: '))
C = K - 273.15
print(f'A temperarura de {K:.2f}ºC corresponde a {C:.2f}K.')
print('Fim')