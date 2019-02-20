#include <stdio.h>
#include <stdlib.h>

class Grade {
 public:
  Grade() {
    printf("產生一個 Grade 物件並將值設為 0\n");
    data_ = 0;     
  }
  Grade(int v) {
    printf("產生一個 Grade 物件並將值設為 %d\n", v);
    data_ = v; 
  }
  ~Grade() {
    printf("釋放一個 Grade 物件\n");
  }
 
 public:
  void Set(int v) {
    data_ = v;
  }
  int Get() const {
    return data_;
  }

 private:
  int data_;
};
 
int main() {
  {
    Grade a;
    Grade b = Grade();
    Grade c[3];

    printf("a = %d\n", a.Get());
    printf("b = %d\n", b.Get());
    for (int i = 0; i < 3; ++i){
      printf("c[%d] = %d\n", i, c[i].Get());
    }
  } // a, b, c 的生命週期在這裡結束 
  system("pause");

  {
    Grade d(10);
    Grade e();       // 此時 e 會被當作一個函式名稱 
    Grade f = Grade(10);
    Grade g = 10;
    printf("d = %d\n", d.Get());
    printf("e = %d\n", e.Get());  // [編譯錯誤] 請移除此行 
    printf("f = %d\n", f.Get());
    printf("g = %d\n", g.Get());
  } // d, f, g 的生命週期在這裡結束 
  system("pause");

  return 0;
} 
