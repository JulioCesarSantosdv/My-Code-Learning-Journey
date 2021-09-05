/*Precisão de exibição de dados em em C*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x = 450;
    float f = 250.12345;
    char s[] = "Linguagem C";
    
   printf(" Precisão em inteiros:\n");
   printf("%10.5d\n",x);// alocado 10 espaços e exibir dados em apenas 5
   printf("%15.12d\n",x);// alocado 15 espaços e exibir dados em apenas 12
   printf("%10.5d\n",x);
   printf("\n\nPrecisão em ponto flutuante:\n");
   printf(" %8.2f\n",f);// alocado 8 espaços e exibir dados em apenas 2
   printf("Precisão em strings:\n");
   printf("%10.5d\n",s);
   
   
   return 0;
}