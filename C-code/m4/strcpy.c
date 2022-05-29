#include<stdio.h>
#include <string.h>
//incomplete
void strcpy1 (char *dest, char *src)
{
    strcpy(src, "Hola ")
	strcpy(*dest, *src)//destination first then what we copy second
}
int main()
{
char array[5]={'H','E','l','L','O','W','o','r','l','d'};
char Narray[5];
strcpy1(Narray, array);
printf("new stringis: %s", Narray);
}
