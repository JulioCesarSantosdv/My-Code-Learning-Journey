/*Operadores e Expressões Aritméticas em C*/

#include <stdio.h>
#include <stdlib.h>
#include<math.h>

int main()
{
    int X, Z , W, K, M, N,P;
    float F;
    X = -2*3;
    Z = 4%2;
    W = 8/4;
    K = 7/2;
    M = W + X;
    F = 7.0/2.0;
    N = M-K;
    P = pow(W,3);
    printf("X: %d\n",X);
    printf("Z: %d\n",Z);
    printf("W: %d\n",W);
    printf("K: %.1f\n",K);
    printf("M: %d\n",M);
    printf("N: %d\n",N);
    printf("F: %.2f\n",F);
    printf("P: %d\n",P);
    
   return 0;
}

