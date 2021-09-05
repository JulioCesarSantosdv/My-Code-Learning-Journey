"""
Ler dois valores numéricos inteiros (representados pelas variáveis A e B) e
apresentar o resultado do quadrado da diferença do primeiro valor (variável A)
em relação ao segundo valor (variável B).
===============================================================================
Entendimento:
1.Ler dois números inteiros(A,B)
2.Calcular (A-B)**2
3.Escrever o resultado.
"""
A = int(input('Digite um número inteiro: '))
B = int(input('Digite um número inteiro: '))
R = (A-B)**2
print(f'O resultado entre a diferença entre {A} e {B} ao quadrado é {R}. ')