#include <iostream>
#include <vector>
#include <algorithm>
#include <forward_list>

using namespace std;

bool cmp(int a, int b) {
    return a > b;
}

int main(){
    vector<int> c = {1,7,2,5,3};
    sort(begin(c), end(c)); //parameters should be Random-access iterators

    for (auto v:c) {
        cout << v << endl;
    }
    
    forward_list<int> ls={1,7,2,5,3};
    ls.sort(); //the specialized sort for linked-list.
    for (auto v:ls){
        cout << v << endl;
    }
    
    int arr[]={1,7,5,3,2};
    sort(begin(arr), end(arr), cmp);
    for (auto v:arr){
        cout << v << endl;
    }
    
    
    return 0;
};


// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4:
