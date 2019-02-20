#include <iostream>
#include <stdlib.h>
#include <vector>
using namespace std;
/*
See the constructor types for vector:
http://www.cplusplus.com/reference/vector/vector/vector/
*/
int main(){
    vector<int> a; //call empty container constructor (default constructor) 
    cout << "a.size()=" << a.size() << endl; //size of a is 0.
    
    vector<int> b(10); //call fill constructor that fills container with 0-value.
    cout << "b.size()=" << b.size() ;
    cout << "; b[0] =" << b[0] << endl;
    
    vector<int> c = {1,2,3,4}; //call initializer list constructor.
    cout << "c.size()=" << c.size() << " ;";
    cout << "c[2]=" << c[2] << endl; //call operator[] meber function.
    
    c[2] = 0;
    cout << "c[2]=" << c[2] << endl; //call operator= copy assignment.
    
    a.resize(3); //resize a = {0,0,0}.
    a.push_back(10); //
    cout << "a.size()=" << a.size() << endl;
    cout << "a[a.size()-1]=" << a[a.size()-1] << endl;


    //C-style array:
    int ca[0]; //ca is a C-array with size of 0.
    cout << "sizeof(ca)/sizeof(int)="<< sizeof(ca)/sizeof(int)<< endl;
    int cb[10]={}; //cb with initializer of zero-values.
    cout << "sizeof(cb)/sizeof(int)="<<  sizeof(cb)/sizeof(int)<<endl;
    cout << "cb[0]=" << cb[0] << endl;
    int cc[]={1,2,3,4}; //cc with initalizer.
    cout << "sizeof(cc)/sizeof(int)=" << sizeof(cc)/sizeof(int)<<endl;
    cout << "cc[2]=" << cc[2] << endl;
    cc[2] = 0;
    cout << "cc[2]=" << cc[2] << endl;

    return 0;
}



// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=85:
