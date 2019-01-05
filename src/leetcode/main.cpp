#include <stdio.h> //preprocessor: do copy/paste for header.
#include <iostream>
#include <string> //for string
#include <algorithm> //for std::reverse
using namespace std; 


class Solution {
public:
    string reverseString(string s) {
        reverse(begin(s), end(s));
        return s;
    }
};

int main(){
    //printf("");
    //std::cout << "h e" <std::endl;
    //cout << "h e" <endl;
    Solution sol;
    if (sol.reverseString("Hello")== "olleh"){
        cout << "Success!\n" ;
    };
    return 0;

}
