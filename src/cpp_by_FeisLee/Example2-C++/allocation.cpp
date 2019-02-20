#include <stdio.h>
#include <stdlib.h>

class Grade {
 public:   
  Grade() {   // 預設建構式 (default constructor) 
    printf("配置一個 Grade 物件\n"); 
    data_ = 0;
  } 
  ~Grade() {  // 解構式 (destructor) 
    printf("釋放一個 Grade 物件\n"); 
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

int main() {
  { 
    Grade g;       // 呼叫建構式 Grade(); 
    printf("Grade: %d\n", g.Get());
    g.Set(100);
    printf("Grade: %d\n", g.Get());
  } // g 的生命週期結束, 呼叫解構式 ~Grade(); 
  system("pause");
  return 0;
} 
