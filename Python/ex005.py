"""
Elabore um programa que efetue o cálculo da quantidade
de litros de combustível gasta em uma viagem , utilizando um automóvel que faz
12 quilômetros  por litro. Considere a fórmula para distância percorrida,
DISTÂNCIA = TEMPO*VELOCIDADE.Apartir do valor da distância,calcule
quantidade de litros LITROS_USADOS = DISTANCIA/12.O programa deve apresentar
os valores da velocidade média, tempo gasto na viagem,a distância percorrida
e a quantidade de litros utilizada na viagem.
==============================================================================
Entendimento:
1.Fazer a leitura de Tempo como um número real
2.Fazer a leitura de Velocidade como um número real
3.Calcule distancia percorrida conforme a fórmula.
4.Calcule litros usados conforme a fórmula
5.Escreva: Velocidade,Tempo,Distância,Litros_Usados
"""
TEMPO = float(input('Informe o tempo gasto: '))
VELOCIDADE = float(input('Informe a velocidade média: '))
DISTANCIA = TEMPO*VELOCIDADE
LITROS_USADOS = DISTANCIA/12.0
print(f'A velocidade média é de {VELOCIDADE},'
      f'\n o tempo gasto é de  {TEMPO}, '
      f'\n a distância percorrida é de {DISTANCIA},'
      f' \n a quantidade de litros usuados foi de {LITROS_USADOS:.2f}.  ')
print('FIM')
