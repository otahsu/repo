#include "sort.h"

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

void quickSort(int number[], int left, int right) { 
    if(left < right) { 
        int s = number[(left+right)/2]; 
        int i = left - 1; 
        int j = right + 1; 

        while(1) { 
            while(number[++i] < s) ;  // 向右找 
            while(number[--j] > s) ;  // 向左找 
            if(i >= j) 
                break; 
            SWAP(number[i], number[j]); 
        } 

        quickSort(number, left, i-1);   // 對左邊進行遞迴 
        quickSort(number, j+1, right);  // 對右邊進行遞迴 
    } 
} 
