#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>

using namespace std;

int main(){
    vector<int> nums = {3,7,5,1,9};
    
    #if 0
    // create a null set.
    set<int> table;

    for ( auto it=begin(nums); it!=end(nums); ++it){
        table.insert(*it);
    }
    #else
    set<int> table(begin(nums), end(nums));
    
    #endif

    // use count() to find whether the target value is in it.
    cout << table.count(3) << endl;
    cout << table.count(4) << endl;
   
    // traverse the sorted elements.
    #if 0
    for (auto p = begin(table); p!=end(table); ++p){
        cout << *p << endl;
    }
    #else
    for (int num: table){
        cout << num << endl;
    }
    #endif
    
    map<int,int> dict; // create a null mapping.
    
    for (int i=0; i < nums.size(); ++i){
        dict[i] = nums[i]; // can insert directly.
    }
    
    cout << dict.count(3) << endl;
    cout << dict.count(4) << endl;

    // traverse the sorted key-value(first).
    for (auto kvp : dict){
        cout << kvp.first << ":" << kvp.second << endl;
    }
    
    map<string, int> sparseArray;

    sparseArray["John"] = 9;
    sparseArray["Mary"] = 7;

    cout << sparseArray["John"] << endl;
    return 0;
}
// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4:
