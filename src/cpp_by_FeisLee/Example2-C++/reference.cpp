#include <stdio.h>
#include <stdlib.h>

int main() {
  int a = 0;
  printf("a: %d\n", a);

  // 使用一般型態 
  int b = a;
  b = 1;
  printf("a: %d\n", a);

  // 使用指標 
  int *c = &a;
  *c = 2;
  printf("a: %d\n", a);

  // 使用參考 
  int &d = a;
  d = 3;
  printf("a: %d\n", a);

  system("pause");
  return 0;
} 
