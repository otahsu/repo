#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){

    auto i = 0; //會自動推測i為int
    int i = 3;
    i < 3 == (int) 0; //C
    i < 3 == (bool) false; //C++, 但false隱性轉型為0
    3 > 2 > 1;
    1 > 1 == 0
    
    //找3的idx的iterator版本
    vector<int> v={1,2,3,4};
    
    //C++11後begin()裡面可以丟C-array    
    int v[4] = {1,2,3,4}

    for (auto p = begin(v); p!=end(v); p++) {
        cout << *p << endl;
    }
    return 0 ;
}
