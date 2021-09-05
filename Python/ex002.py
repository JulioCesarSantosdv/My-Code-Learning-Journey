"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus
Celsius.A fórmula de conversão é C= ((F - 32)*5)/9,sendo F a temperatura em
Fahrenheit e C a temperatura em Celsius.
========================================================================
Entendimento
1.Fazer a leitura de F como número real
2.Calcular C mediante a fórmula
3.Escreva C
"""
F = float(input('Informe a temperatura em ºF: '))
C = ((F-32)*5)/9
print(f'A temperatura de {F:.1f}ºF corresponde a {C:.1f}°C.')
print('FIM')