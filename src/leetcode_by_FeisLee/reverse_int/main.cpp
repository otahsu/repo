#include <iostream>
#include <stdlib.h>
#include <vector>
using namespace std;

/*
To cosider overflow, use std::numeric_limits template for a given type.
http://www.cplusplus.com/reference/limits/numeric_limits/

*/

class Solution {
public:
    int reverse(int x) {
        long long r=0;//if r is int, may be overflow.
        while (x !=0){
            int d = x % 10;
            x /= 10;
            r = r*10 + d; 
            if ( r < numeric_limits<int>::min() || r > numeric_limits<int>::max() )
                return 0;
        }
        return r;
    }

};

int main(){
    Solution sol;

    cout << sol.reverse(-12345) << endl;
    cout << "int min()=" << numeric_limits<int>::min() << endl;
    cout << "int max()=" << numeric_limits<int>::max() << endl;
    cout << "non-signed bits of long long=" << numeric_limits<long long>::digits << endl;

    cout << sol.reverse(-1023456789) << endl; //int-overflow: return 0.

    return 0;
}



// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4:
