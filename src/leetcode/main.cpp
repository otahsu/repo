#include <stdio.h> //preprocessor: do copy/paste for header.
#include <iostream>
#include <string> //for string
#include <algorithm> //for std::reverse
using namespace std; 


class Solution {
public:
    string reverseString(string s) {
        //reverse(begin(s), end(s));
        string r; // r is not ary.
        r[3] = 'a'; // r.operator[](3) //it's op overload.
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
    
    int a; //primary type: no defualt constuctor, and the initial value is not sure.
    int ******a[3]; //right first: so it's a array of pointer, not pointer.
    string s; //call defalt constructor, size is 0.

    int a[3] = {1,2,3}; //def: a iff is a array only when[] is after.
    // a[b] <==> *(a+b) 
    1[a]; //it eq to a[1]; 
    return 0;

}
