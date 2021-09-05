/*Criando funções em C*/

#include <stdio.h>
#include <stdlib.h>
#include locale.h

 void escrevaNome();
 int main()
 {
     setlocale(LC_ALL,"");
     escrevaNome();
     escrevaNome();
     escrevaNome();
     return 0;
 }
 
 void escrevaNome(){
     printf("Bem vindo ao meu app \n");
     return 0;
     
 }