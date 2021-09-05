"""
Construir um programa que leia três valoes numéricos inteiros e apresente
como resultado final o valor da soma dos quadrados dos três valores lidos.
=============================================================================
Entendimento
1.Ler três valores inteiros (A,B,C)
2.Somar os quadrados dos 3 valores (A**2)+(B**2)+(C**2)
3.Receber essa soma numa variável (R)
4.Escrever R
"""
A = int(input('Informe um número: '))
B = int(input('Informe um outro número: '))
C = int(input('Informe um outro número: '))
R = (A**2)+(B**2)+(C**2)
print(f'Soma dos quadrados de {A}, {B} , {C}, é {R}.')
