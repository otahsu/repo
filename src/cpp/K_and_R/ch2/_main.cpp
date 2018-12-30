#include <stdio.h>
#include "typesize.h"

int main(int argc, char** argv)
{
    /* use sizof() to count the byte-number for build-in types*/
    printf("The size of char = %d\n", sizeof(char));
    printf("The size of short = %d\n", sizeof(short));
    printf("The size of long = %d\n", sizeof(long));
    printf("The size of short int = %d\n", sizeof(short int));
    printf("The size of int = %d\n", sizeof(int));
    printf("The size of short int = %d\n", sizeof(long int));
    printf("The size of float = %d\n", sizeof(float));
    printf("The size of double = %d\n", sizeof(double));
    printf("The size of long double = %d\n", sizeof(long double));
    
    /* Use my function */
    printf("====================================\n");
    //TODO-memo: %d is to print a data-object by explaning it as 'digit'(number).
    printf("The size of char = %d\n", get_size_of_char()); 
    printf("The size of short = %d\n", get_size_of_short()); 
    
    return 0;
}

// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=200: