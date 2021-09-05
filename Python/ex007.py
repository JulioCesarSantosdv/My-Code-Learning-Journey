"""
Leia dois valores para as variáveis A e B e efetue a troca de valores de forma
que a variável A passe a possuir o valor da variável B e a variável B passe a
possuir o valor da variável A.Apresente os valores após a efetivação do
processamento de traca.
===============================================================================
Entendimento
1.Fazer a leitura  de A,B
2.Fazer com que X receba A
3.Fazer com que A receba B
4.Fazer com que B receba X
5.Escreva A,B
"""
A = int(input('Informe um número: '))
B = int(input('Informe um número: '))
print(f'A letra A vale {A} e a letra B vale {B}')
X = A # Aqui é feita a troca.
A = B
B = X
print(f'{X} - {A} - {B}')
print(f'Agora a letra A vale {A} e a letra B vale {B}.')



