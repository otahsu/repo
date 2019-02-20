#include <algorithm>
#include <map>

bool cmp(int a, int b){
    if(a%2==1 && b%2==1)
        return a<b;
        .....

}

int main() {
    //vector<int> a[8];

    map<int, int> a;//map<key, value>不用管size的問題
    a[3] = 10; //排序是用第一個key idx的大小去排
    a[7] = 6;  //map[key] = value
    
    //奇數在前偶數在後，奇數遞增，偶數遞減
    int v[]={1,2,8,9,3,2}
    sort(begin(v), end(b), cmp)

}

// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4:
