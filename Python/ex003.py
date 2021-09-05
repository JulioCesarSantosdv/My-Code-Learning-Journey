"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus
Kelvin.A fórmula de conversão é K = C + 273.15,sendo K a temperatura em
Kelvin e C a temperatura em Celsius.
=============================================================================
Entendimento
1.Fazer a leitura de C como um número real
2.Calcule K mediante a fórmula
3.Escreva K
"""
C = float(input('Informe uma temperatura em °C: '))
K = C + 273.15
print(f'A temperarura de {C:.1f}ºC corresponde a {K:.2f}°K.')
print('Fim')



