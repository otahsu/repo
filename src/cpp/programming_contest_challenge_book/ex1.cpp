#include <stdio.h>
#include <stdlib.h>
#define MAX 1000

typedef struct Triangle
{
    // the edge-lengths are ordered in acsending.
    int a, b, c;
} Triangle;

int get_arc_length(Triangle Tri)
{
    int arc = Tri.a + Tri.b + Tri.c;
    return arc;
}

int intAry[MAX] = {0};
int main(int argc, char** argv)
{
    printf("intAry[MAX-1] = %d\n", intAry[MAX-1]);
    int dNum_edge = 5;
    int* pEdgeAry = (int*) malloc(sizeof(int)*dNum_edge);
    char* sInput[5];
    int i,j,k=0;
    Triangle TriAry[3] = { {1,1,1,}, {2,2,2}, {3,3,3} }; 
    /*
    while( i < dNum_edge )
    {
       sInput[i]= getchar();
       i += 1;
    }
    printf("sInput = %s\n", sInput);
    */
    pEdgeAry[0] = 1; 
    pEdgeAry[1] = 2; 
    pEdgeAry[2] = 3; 
    pEdgeAry[3] = 4; 
    pEdgeAry[4] = 5;
    printf("TriAry[0].c = %d\n", TriAry[0].c);
    
    for( i=0 ; i< 3 ; i++)
    {
        int dArc = get_arc_length( TriAry[i] );
        printf("The arc of TriAry[%d] = %d\n", i, dArc);

    }
}

// vim : set ft=cpp ff=unix fenc=utf8 ai et sw=4 ts=4 tw=79:
