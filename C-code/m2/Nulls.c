#include<stdio.h>

int main()

{
	char arrChar[6] = {'a','b','\0','d','e','f','G','\0'};
	char arrString2[] = "ABCDEFG";
    int array[] = {1,2,3};
	memset(arrChar[3], '\0');//check this out

    char spill = "spill";
	char over = {'o','v','e','r'};

	printf("Printed arrChar is:%s\n", arrChar);
	printf("Printed arrString2 is:%s\n", arrString2);

	for(int count = 0; count < 10; count++)//10 is intentailly too high
		printf("arrchar[%d]: %c Address: %p\n", count, arrChar[count], &arrChar[count]);
        printf("arrString[%d]: %c Address: %p\n", count, arrChar[count], &arrChar[count]);
        printf("arrchar[%d]: %c Address: %p\n", count, arrChar[count], &arrChar[count]);
		
		////Pointers only below////
	int  *ptr = NULL;
	
	printf("Value of ptr is : %x\n", ptr  );
	if(ptr)     /* is not null */
		printf("Pointer!!");
	if(!ptr)    /* is null */
		printf("NULL!!");
	return(0);

}
