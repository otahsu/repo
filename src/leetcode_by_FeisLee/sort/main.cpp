/*
    Sample C-code from 良葛格:
    https://openhome.cc/Gossip/AlgorithmGossip/SelectionInsertionBubble.htm
    See the antimation demo on visulago:
    https://visualgo.net/en/sorting

*/

#include <stdio.h> 
#include <stdlib.h> 
#define LEN 8 
#define SWAP(x,y) {int t; t = x; x = y; y = t;} 

void selectionSort(int*, int, int(*)(int, int));
void insertionSort(int*, int, int(*)(int, int));
void bubbleSort(int*, int, int(*)(int, int));

void print(int*, int len);
int ascending(int, int);  //compare function.
int descending(int, int); //compare function.

int selectedIdx(int* arr, int from, int to, int(*compar)(int, int)) {
    int selected = from;
    int i;
    for(i = from + 1; i < to; i++) if(compar(arr[i], arr[selected]) < 0) {
        selected = i;
    }
    return selected;
}

void selectionSort(int* arr, int len, int(*compar)(int, int)) { 
    int i;
    for(i = 0; i < len; i++) {
        int selected = selectedIdx(arr, i, len, compar);
        if(selected != i) { SWAP(arr[i], arr[selected]) }
    }
} 

int insertedIdx(int* arr, int eleIdx, int(*compar)(int, int)) {
    int i;
    for(i = 0; i < eleIdx; i++) if(compar(arr[i], arr[eleIdx]) > 0) { 
        break; 
    }
    return i;
}

void insert(int* arr, int eleIdx, int inserted) {
    int ele = arr[eleIdx];
    int i;
    for(i = eleIdx; i > inserted; i--) { arr[i] = arr[i - 1]; }
    arr[inserted] = ele; 
}
 
void insertionSort(int* arr, int len, int(*compar)(int, int)) {
    int i;
    for(i = 0; i < len; i++) {
        int inserted = insertedIdx(arr, i, compar);
        if(inserted != i) { insert(arr, i, inserted); }
    }
}

void bubbleTo(int* arr, int to, int(*compar)(int, int)) {
    int i;
    for(i = 0; i < to - 1; i++) if(compar(arr[i + 1], arr[i]) < 0) {
        SWAP(arr[i + 1], arr[i]);
    }
}

void bubbleSort(int* arr, int len, int(*compar)(int, int)) {
    int i;
    for(i = 0; i < len; i++) { bubbleTo(arr, len - i, compar); }
}

void print(int* arr, int len) {
    int i;
    for(i = 0; i < len; i++) { printf("%d ", arr[i]); } 
    printf("\n");
}

int ascending(int a, int b) { return a - b; }
int descending(int a, int b) { return -ascending(a, b); }

int main(void) {  
    int number[LEN] = {10, 9, 1, 2, 5, 3, 8, 7}; 
    
    selectionSort(number, LEN, ascending);
    print(number, LEN);
    
    insertionSort(number, LEN, descending);
    print(number, LEN);
    
    bubbleSort(number, LEN, ascending);
    print(number, LEN);
        
    return 0; 
} 




// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4:
