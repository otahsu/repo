#include <iostream>
using namespace std;
void foo();

int main(int argc, char** argv) {
    foo();
    cout << "hello world" << endl;
    cout << "print out the " << argc << " arguments" << endl;
    for(int i=0; i < argc; i++) { 
        cout << argv[i] << ", ";
    };
    cout << endl;
    foo();
    return 0;
}

