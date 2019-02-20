#include <stdio.h>
#include <stdlib.h>

void Print(int v) {
  printf("%d\n", v);
}

void Print(float v) {
  printf("%f\n", v);
}

void Print(char v) {
  printf("%c\n", v);
}
 
int main() {
  Print(3);
  Print(3.f);
  Print('3');

  Print(3.);  // [½sÄ¶¿ù»~] ©I¥s­þ­Ó Print ?
  system("pause");
  return 0;
} 
