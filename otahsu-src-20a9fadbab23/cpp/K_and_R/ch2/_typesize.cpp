#include "typesize.h"
#include <stdio.h>
//#include <limits.h>
//#include <float.h>
#include <stdlib.h>
#define MAX 100
#define ONE_BYETE_UPPER_BOUND  127
#define ONE_BYETE_LOWER_BOUND -128
#define TWO_BYETE_UPPER_BOUND  32767
#define TWO_BYETE_LOWER_BOUND -32768

/***********************************/
int get_size_of_char()
{ 
    char c;
    int i;
    char s1[MAX], s2[MAX];
    
    // TODO-memo: On 2's complement machine, c is over-flow.
    c = ONE_BYETE_UPPER_BOUND + 1;
    sprintf(s1, "%d", c);
    c = ONE_BYETE_LOWER_BOUND -1;
    sprintf(s2, "%d", c);
    printf("s1, s2 = %s, %s\n", s1, s2);
    
    //TODO-memo: The boundary-condisiont uses the charateristic of over-flow.
    if ( (i=atoi(s1)) == ONE_BYETE_LOWER_BOUND && (i=atoi(s2)) == ONE_BYETE_UPPER_BOUND) 
        return 1;
    else
        return 0;
}
/***********************************/
int get_size_of_short()
{ 
    short c;
    int i;
    char s1[MAX], s2[MAX];
    
    // TODO-memo: On 2's complement machine, c is over-flow.
    c = TWO_BYETE_UPPER_BOUND + 1;
    sprintf(s1, "%d", c);
    c = TWO_BYETE_LOWER_BOUND -1;
    sprintf(s2, "%d", c);
    printf("s1, s2 = %s, %s\n", s1, s2);
    
    //TODO-memo: The boundary-condisiont uses the charateristic of over-flow.
    if ( (i=atoi(s1)) == TWO_BYETE_LOWER_BOUND && (i=atoi(s2)) == TWO_BYETE_UPPER_BOUND) 
        return 2;
    else
        return 0;
}
int get_size_of_int()
{ return 0 ;}
int get_size_of_long()
{ return 0 ;}

// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=100:
