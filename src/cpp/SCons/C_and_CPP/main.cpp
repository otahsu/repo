#include "c_api.h"
#include <iostream>
using namespace std;

int main( int argc, char** argv )
{
    #if 0
    cout << "hello world" << endl;
    cout << "print out the 2 arguments" << endl;
    cout << argv[0] << ", " << argv[1] << ", " << argv[2] << ", " << endl;
    #endif
    // test c_api
    char* buf="cstring";
    C_print( buf);

    return 0;
}

//vim: set ft=cpp ai ts=4 et sw=4 sts=4 tw=85:
