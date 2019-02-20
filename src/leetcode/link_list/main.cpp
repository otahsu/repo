#include <stdio.h>
#include <forward_list>
#include <iostream>
#include <algorithm>

using namespace std;

class ListNode {
public:
    int val;
};


int main(){
    int *r = NULL; //C macro NULL==0 
    int *q = nullptr; //C++'s null pointer
    
    forward_list<int> a = {1,2,3};
    a.reverse();
    
    a.insert_after(a.before_begin(), 0);

    for (auto p = begin(a); p !=end(a); p++){
        cout << *p << endl;
    }

    return 0;
}




// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4:
