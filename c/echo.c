#include <stdio.h>

// DESCRIPTION
//   echo - print arguments to stdout
// SYNOPSIS
//   echo [STRING]...
// BUILDING
//   $ gcc -o echo echo.c

int main(int argc, char *argv[]) {
  for (int i = 1; i < argc; ++i) {
    if (i > 1) {
      printf(" ");
    }

    printf("%s", argv[i]);
  }
  printf("\n");

  return 0;
}
