"""
Construir um programa que leia três valores numéricos inteiros e apresente
como resultado final o valor do quadrado da soma dos três valores lidos.
==============================================================================
Entendimento:
1.Ler três valores inteiros
2.Resultado da soma dos valores ao quadrado(A+B+C)**2
3.Receber esse valor numa variável (R)
4.Escrever R
"""
A = int(input('Informe um número: '))
B = int(input('Informe um outro número :'))
C = int(input('Informe um outro número: '))
R = (A**2)+(B**2)+(C**2)
print(f'O valor do quadrado da soma de {A}, {B} ,{C} é {R}. ')