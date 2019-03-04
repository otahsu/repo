/*
    Sample C-code from 良葛格:
    https://openhome.cc/Gossip/AlgorithmGossip/SelectionInsertionBubble.htm
    https://openhome.cc/Gossip/AlgorithmGossip/QuickSort2.htm
    See the antimation demo on visulago:
    https://visualgo.net/en/sorting

*/

#include "sort.h"

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
