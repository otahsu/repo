#include <cstdlib>
#include <iostream>

class Grade {
 public:
  Grade() { data_ = 0; }  
  Grade(int v) { data_ = v; }

  void Set(int v) { data_ = v; }
  int Get() const { return data_; }
 
 private:
  int data_;
};
 
std::ostream& operator<<(std::ostream &lhs, const Grade &rhs) {
  lhs << rhs.Get();
  return lhs;
}

std::istream& operator>>(std::istream &lhs, Grade &rhs) {
  int x;
  lhs >> x;
  rhs.Set(x);
  return lhs;
}

int main() {
  using namespace std;
  Grade a, b;
  cout << "請依序輸入兩個成績: "; 
  cin >> a >> b;
  cout << "這兩個成績為 " << a << " 和 " << b << endl; 
  system("pause");
  return 0;
} 
