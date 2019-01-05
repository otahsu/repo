#include <stdio.h> //preprocessor: do copy/paste for header.
#include <iostream>
#include <string> //for string
#include <algorithm> //for std::reverse
#include <vector> //for std::vector

using namespace std; 


class Solution1 {
public:
    string reverseString(string s) {
        reverse(begin(s), end(s));
        //string r; // r is not ary.
        //r[3] = 'a'; // r.operator[](3) //it's op overload.
        
        return s;
    };
};

class Solution2 {
public:
    string reverseString(string s){
        string r;
        r.resize(s.size());
        for (int i = 0; i < r.size(); ++i){
            r[i] = s[s.size()-1-i];
        }
        return r;
    }

};

class Solution3 {
public:
    string reverseString(string s){
        for (int i = 0; i < s.size()/2; ++i){
            char c = s[i]; //do swap
            s[i] = s[s.size()-1-i];
            s[s.size()-1-i] = c;
        }
        return s;
    }

};

int main(){
    //printf("");
    //std::cout << "h e" <std::endl;
    //cout << "h e" <endl;
    Solution1 sol1;
    if (sol1.reverseString("Hello") == "olleH"){
        cout << "ver1 Success!\n" ;
    };
    
    Solution2 sol2;
    if (sol2.reverseString("Hello") == "olleH"){
        cout << "ver2 Success!\n" ;
    }
    
    Solution3 sol3;
    if (sol3.reverseString("Hello") == "olleH"){
        cout << "ver3 Success!\n" ;
    }
    return 0;
}

// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=85:

