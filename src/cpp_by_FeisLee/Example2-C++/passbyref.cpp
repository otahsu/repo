#include <stdio.h>
#include <stdlib.h>

int &Clear(int &v) {
  v = 0;
  return v;
}
 
int main() {
  int v = 3;
  printf("v: %d\n", v);
  Clear(v);
  printf("v: %d\n", v);

  Clear(v) = 4;
  printf("v: %d\n", v);
 
  system("pause");
  return 0;
} 
