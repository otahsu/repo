#include <cstdio>
#include <cstdlib>

using namespace std;

namespace A {
  void B() { 
    printf("執行 ::A::B()");
  }
  void C() {  
    printf("執行 ::A::C() -> ");
    printf("呼叫 B() -> "); 
    B();     
  }
}

void B() { 
  printf("執行 ::B()"); 
}

int main() { 
  printf("執行 ::main \n");

  printf("呼叫 B() -> ");  
  B();   // 會試著呼叫 ::B() 和 ::std::B() -> 結果是 ::B() 
  printf("\n");

  printf("呼叫 ::B() -> "); 
  ::B(); // 會試著呼叫 ::B()
  printf("\n");

  printf("呼叫  A::B() -> "); 
  A::B(); // 會呼叫 ::A::B() 和 ::std::A::B() -> 結果是 ::A::B() 
  printf("\n");

  printf("呼叫 ::A::B() -> "); 
  ::A::B(); // 會呼叫　::A::B() 
  printf("\n");

  printf("呼叫 A::C() -> "); 
  A::C();   // 會呼叫  ::A::C() 和 ::std::A::C() -> 結果是 ::A::C() 
  printf("\n");

  printf("呼叫 ::A::C() -> "); 
  ::A::C(); // 會呼叫  ::A::C() 
  printf("\n");

 
  using namespace A;
  // using A::B;
  // using ::B;
  printf("呼叫 B() -> ");  
  B();     // [編譯錯誤] 這裡的 B() 有幾種可能 ?   怎麼辦 ? 
  printf("\n");

  printf("呼叫 ::B() -> "); 
  ::B();
  printf("\n");

  system("pause");
  return 0;
}
