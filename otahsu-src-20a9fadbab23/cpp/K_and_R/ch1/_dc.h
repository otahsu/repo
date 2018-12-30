#ifndef __DC__
#define __DC__
#include <stdio.h>

/* K&R P.22 : count digits, white space, others */
void count_digits()
{
    int c, i, nwhite, nother;
    int ndigit[10];
    printf("The decimal value of \'0\' = %d\n", '0');
    // Initailize variables as zeros.
    nwhite = nother = 0;
    for (i = 0; i < 10; ++i)
        ndigit[i] = 0;
    while ( (c = getchar()) != EOF)
    //{ //TODO: why does it need no braces{ }?
        //TODO-memo : The precedence of logic-opertor is higher than
        //arithmetic-operator.
        if (c >= '0' && c <= '9') 
            ++ndigit[c-'0'];//TODO-memo :int exprssion for a subscript(index) is OK.
        else if (c == ' ' || c == '\n' || c == '\t')
            ++nwhite;
        else
            ++nother;
    //}
    printf("digit occurrences table =\n0, 1, 2, 3, 4, 5, 6, 7, 8, 9\n");
    for (i = 0; i < 10; ++i)
        printf("%d, ", ndigit[i]);
    printf("\nwhite space = %d\nother char = %d\n", nwhite, nother);
}
#endif
// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=200: