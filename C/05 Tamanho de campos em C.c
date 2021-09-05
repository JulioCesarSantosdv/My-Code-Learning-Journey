/*Tamanhos de Campos em C*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
 
   printf(" %d\n",6);
   printf(" %5d\n",6);
   printf(" %10d\n",6);
   printf(" %10d\n",700);
   printf(" %c\n",'T');
   printf(" %1c\n",'A');
   printf(" %2c\n",'B');
   printf(" %3c\n",'C');
   printf(" %4c\n",'D');
   printf(" %-4c\n",'F');// Alinhando a esquerda com o sinal de menos
   printf(" %10f\n",23.8); // Exibe 10 casas decimais
   
   
   return 0;
}