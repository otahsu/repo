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
        //r[3] = 'a'; // r.operator[](3) //it's op overload.
        
        }
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
    
    // C-style ary
    int a[3];
    // C++ style array
    int 
    // C-style string

    int a[] = {3,4,5};// C-stryle ary initalizer.
    vector<int> b(3); // b is objector, vector, is c++-array 
    vector<int> b = {3,4,5}; // b is objector, vector, is c++-array.After C++11 vector can use list-initializer. 
    vector<int> b(3); // b is objector, vector, is c++-array size of 3, initalize to 0,0,0. 
    
    return 0;

}
