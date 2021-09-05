"""
Elabore um programa que calcule e apresente o valor do resultado da área de uma
circunferência(A).O programa deve solicitar a entrada do valor do raio da
circunferência(R).Para a execução deste problema utilize a fórmula
A = 3.14159265 * R ** 2.
=================================================================================
Entendimento
1.Ler o valor do raio da circunferência(R) como número real
2.Calcular a área (A) conforme a fórmula
3.Escreva A
"""
R = float(input('Informe o valor do raio da circunferência: '))
A = 3.14159265 * R ** 2
print(f'Um raio de circunferência de {R:.2f} tem uma  área da circunferência de {A:.2f}')
