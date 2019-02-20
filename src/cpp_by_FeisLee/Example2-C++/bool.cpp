#include <stdio.h>
#include <stdlib.h>

int main() {
  if (true) {
    printf("True\n");
  }

  if (false) {
    printf("False\n");
  }

  bool a = (3 == 3);  // 實際上這裡( ) 可以省略 

  if (a) {
    printf("3 == 3\n");
  } else {
    printf("3 != 3\n");
  } 

  printf("true: %d\n",  (int) true);  // 實際上這裡的轉型可以省略 
  printf("false: %d\n", (int) false); // 實際上這裡的轉型可以省略 

  system("pause");
  return 0;
} 
