"""
Elaborar um programa que leia quatro valores numéricos inteiros(A,B,C,D).Ao final
o programa deve apresentar o resultado do produto(P) do primeiro com o terceiro
valor e o resultado da soma (S) do segundo com o quarto valor.
=================================================================================
Entendimento:
1.Ler quatro valores inteiros(A,B,C,D)
2.Receber o produto de (A*C) numa variável(P)
3.Receber a soma de (B+D) numa variável(S)
4.Escreva P e S
"""
A = int(input('Informe um número: '))
B = int(input('Informe um outro número: '))
C = int(input('Informe um outro número: '))
D = int(input('Informe um outro número: '))
P = (A*C)
S = (B+D)
print(f'O produto entre {A} e {C} é {P}, a soma entre {B} e {D} é {S}.')
