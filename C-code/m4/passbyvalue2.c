#include<stdio.h>




int swap(int a, int b)
{
int temp;
printf("a: %p b; %p\n", &a, &b);
printf("a: %d b: %d\n", a, b);
temp = a;
a = b;
b = temp;
printf("a: %p b: %p\n", &a, &b);
printf("a: %d b: %d\n", a, b);
return(6);
}

int main()
{
int aval = 100, bval = 200000;
printf("aval: %p bval: %p\n", &aval, &bval);
printf("aval: %d bval: %d\n", aval, bval);

swap(aval, bval);
//not saved upon return as they are local variables unlike arrays or pointers
printf("aval: %p bval: %p\n", &aval, &bval);
printf("aval: %d bval: %d\n", aval, bval);
}


