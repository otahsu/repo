#ifndef _SORT_H_
#define _SORT_H_

#include <stdio.h> 
#include <stdlib.h> 
#include <time.h> 

#define LEN 8 
#define SWAP(x,y) {int t; t = x; x = y; y = t;} 
#define MAX 10


void selectionSort(int*, int, int(*)(int, int));
void insertionSort(int*, int, int(*)(int, int));
void bubbleSort(int*, int, int(*)(int, int));

void print(int*, int len);
int ascending(int, int);  //compare function.
int descending(int, int); //compare function.

void quickSort(int[], int, int); 


#endif
