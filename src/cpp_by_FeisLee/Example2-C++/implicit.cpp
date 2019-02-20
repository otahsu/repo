#include <stdio.h>
#include <stdlib.h>

class Grade {
 public:
  Grade() {
    data_ = 0;
  }
  Grade(int v) {
    data_ = v;
  } 
  void Set(int v) { 
    data_ = v;
  }
  int Get() const { 
    return data_;
  }

 private:
  int data_;
}; 

const Grade Add1(const Grade &lhs, const Grade &rhs) {
  return Grade(lhs.Get()+rhs.Get());
}

const Grade Add2(const Grade &lhs, const Grade &rhs) {
  return lhs.Get()+rhs.Get();     // 這裡會做隱性轉型將 int 轉為 Grade(int) 
}

int main() {
  Grade a = Add1(3, 5);    // 兩個引數分別會隱性轉型成 Grade(3) 及 Grade(5) 
  printf("a: %d\n", a.Get());

  a = 3;       // 這裡會做隱性轉型將 int(3) 轉為 Grade(3) 然後儲存在 a 裡面 
  printf("a: %d\n", a.Get());

  Grade b; 
  b = Add1(a, 5);
  printf("b: %d\n", b.Get());

  Grade c; 
  c = Add2(3, 5);
  printf("c: %d\n", c.Get());

  system("pause");
  return 0;
} 
