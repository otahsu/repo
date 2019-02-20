#include <cstdio>
#include <cstdlib>

// 位於 :: (全域) 的命名空間 

namespace A { // 這個命名空間全名為 ::A
 
  void B() { // 這個函式的全名為 ::A::B() 
    std::printf("執行 ::A::B()");
  }

  void C() { // 這個函式的全名為 ::A::C() 
    std::printf("執行 ::A::C() -> ");
    std::printf("呼叫 B() -> "); 
    B();     // 會試著呼叫 ::A::B() (相對路徑) 
  }
}

void B() { // 全名為 ::B() 
  std::printf("執行 ::B()"); 
}

int main() { // 全名為 ::main()
 
  std::printf("執行 ::main \n"); // 會呼叫 ::std::printf()

  std::printf("呼叫 B() -> ");   
  B();   // 會呼叫 ::B()           (相對路徑) 
  std::printf("\n");
 
  std::printf("呼叫 ::B() -> "); 
  ::B(); // 會呼叫 ::B()           (絕對路徑) 
  std::printf("\n");

  std::printf("呼叫 A::B() -> "); 
  A::B(); // 會呼叫 ::A::B()       (相對路徑) 
  std::printf("\n");

  std::printf("呼叫 ::A::B() -> "); 
  ::A::B(); // 會呼叫　::A::B()    (絕對路徑) 
  std::printf("\n");

  std::printf("呼叫 A::C() -> "); 
  A::C();   // 會呼叫  ::A::C()    (相對路徑) 
  std::printf("\n");

  std::printf("呼叫 ::A::C() -> "); 
  ::A::C(); // 會呼叫  ::A::C()    (絕對路徑) 
  std::printf("\n");

  std::system("pause");
  return 0;
}
