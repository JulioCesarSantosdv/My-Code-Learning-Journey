"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus
Fahrenheit.A fórmula de conversão é F=(9*C+160)/5,sendo F a temperatura em
Fahrenheit e C a temperatura em Celsius.
========================================================================
Entendimento
1.Fazer a leitura de C como número real
2.Calcular F mediante a fórmula
3.Escreva F
"""
C = float(input('Digite a temperatura em °C: '))
F = (9*C+160)/5
print(f'A temperatura de {C:.1f}°C corresponde a {F:.1f}°F!')
print('Fim')