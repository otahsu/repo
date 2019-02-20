//need to re-organize.
//190105 1st course
//Fail to compiler these in-class! why?
/*
class CppTypeDemo {
public:
    int a1; //primary type: no defualt constuctor, and the initial value is not sure.
    int ******a2[3]; //right first: so it's a array of pointer, not pointer.
    string s; //call defalt constructor, size is 0.

    int a3[3] = {1,2,3}; //def: a iff is a array only when[] is after.
    // a[b] <==> *(a+b) 
    //1[a]; //it eq to a[1]; 
    
    // C-style ary
    int ary1[3];
    // C++ style array, vector can be resized. default value is 0 in C++, not in C.
    //vector<int,3> ary2; //size is fixed.
    vector<int> v; //size is changable.
     
    // C-style string

    int ary3[] = {3,4,5};// C-style array with initalizer.
    vector<int> b1(3); // b is objector, vector, is c++-array 
    vector<int> b2 = {3,4,5}; // b is objector, vector, is c++-array.After C++11 can use list-initializer. 
    vector<int> b3(3); // b is objector, vector, is c++-array size of 3, initalize to 0,0,0. 

};
*/
//190106 2nd course
int a;
int *c;
int d[3][2];
int *e[3][2]; //ary
int (*f)[5]; //pointer; 遇到()優先;否則右邊先
int (*g[3])[5];

vector<int> h;
vector<vector<int>> v; //vecotor of vector; 










// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=85:
