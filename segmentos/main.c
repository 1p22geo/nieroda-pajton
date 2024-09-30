#include <stdio.h>

int main(int argc, char *argv[]) {
  int data[1000];

  int maxq1 = 0;
  int maxq2 = 0;
  int max = 0;

  FILE *file = fopen("dane1_3.txt", "rt");
  for (int i = 0; i < 1000; i++) {
    int n;
    fscanf(file, "%d", &n);
    data[i] = n;
  }
  printf("data loaded\n");

  for (int q1 = 0; q1 < 1000; q1++) {
    for (int q2 = q1; q2 < 1000; q2++) {
      int sum = 0;
      for (int count = q1; count <= q2; count++) {
        sum += data[count];
      }
      if (sum >= max) {
        maxq1 = q1;
        maxq2 = q2;
        max = sum;
      }
    }
  }

  fclose(file);
  printf("biggest sum: segment from [%d] to [%d]\nsum:[%d]\n", maxq1, maxq2,
         max);

  return 0;
}
