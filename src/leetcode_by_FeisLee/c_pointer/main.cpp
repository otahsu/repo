#include <iostream>
#include <stdlib.h>
#include <vector>


int main(){
    int *p= (int*)123; //undefined behavior. 
    int a = 7;
    printf("p=%d\n", p);
    //*p=a; //Segmentation fault: 11; by now, no memory space is allowed to accecced
            //by pointer p;
    p = &a;
    a = 5;

    printf("p=%d\n", p);
    printf("*p=%d\n", *p);
    
    return 0;
}



// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=85:
