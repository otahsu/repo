#include <stdio.h>
#include <stdlib.h>

class Grade {
 public:
  void Set(int v) { 
    data_ = v;
  }
  int Get() const {   // 這個 const 讓 Get() 可以被 const Grade 呼叫 
    return data_;
  }

 private:
  int data_;
}; 

Grade Add0(Grade lhs, Grade rhs) {                // 函式傳值 
  Grade ret;
  ret.Set(lhs.Get()+rhs.Get());
  return ret;
}

Grade Add1(Grade &lhs, Grade &rhs) {              // 函式傳參考: 比較有效率但有風險 
  Grade ret;
  ret.Set(lhs.Get()+rhs.Get());
  // lhs.Set(0);                                  // Add1 裡面有可能不小心改到引數的本尊 
  return ret;
}

Grade Add2(const Grade &lhs, const Grade &rhs) {  // 函式傳固定值參考 
  Grade ret;
  ret.Set(lhs.Get()+rhs.Get());
  return ret;
}

const Grade Add3(const Grade &lhs, const Grade &rhs) {  // 函式傳固定值參考並回傳固定值 
  Grade ret;
  ret.Set(lhs.Get()+rhs.Get());
  return ret;
}

int main() {
  Grade a, b;
  a.Set(3);
  b.Set(5);

  Grade c;
  c.Set(10);
  Grade d = Add0(Add0(a, b), c);    // 會需要複製很多次 Grade 物件 
  Grade e = Add1(Add1(a, b), c);    // [編譯錯誤] 請移除此行 
  Grade f = Add2(Add2(a, b), c); 
  printf("d: %d\n", d.Get());
  printf("e: %d\n", f.Get());

  Add2(a, b).Set(8);                // 沒有編譯錯誤並不合理 

  Add3(a, b).Set(8);                // [編譯錯誤] 請移除此行 

  printf("%d\n", Add3(a, b).Get()); // 沒有編譯錯誤 

  system("pause");
  return 0;
} 
