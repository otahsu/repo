#include <iostream>
using namespace std;

int main() {
    for (int i=0; i < 4; i++) {
        for (int j=i+1; j < 4; j++) { // To ensure j>i, 6-pairs
           cout << i << ", "<< j << endl; 
        }
    }
    return 0;
}


// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=85:
