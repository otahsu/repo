#include <stdlib.h>
#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i=0; i < nums.size(); i++) { 
        //size_t is a type of unsigned-int, but the size is depending by compiler
        //enviroment. 
            for (int j=i+1; j < nums.size(); j++) {
                if ( nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
    
        return {}; //null case.
    }
};

int main() {

    Solution sol;
    vector<int> nums={1, 2, 8, 9};

    cout << sol.twoSum(nums, 9)[0] << ", " << sol.twoSum(nums, 9)[1]<< endl;

    return 0;
}


// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=85:
