#include <stdio.h>
#include <stdlib.h>


int main() {
  int a = 3;

  int &b = a;         // b 為 a 之參考

  int &c = 3;         // [編譯錯誤]

  const int &d = 3;   // d 是個固定值參考
 
  system("pause");
  return 0;
}
