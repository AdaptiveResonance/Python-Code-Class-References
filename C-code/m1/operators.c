#include <stdio.h>

int main ()
{
	float val, input = 5, input2 = 23;
	int intVal, int1 = 3, int2 = 5;
	
	float sum = input + input2;
	printf("Float sum = %f\n", sum);//Prints Float sum = 28.0000
	
	printf("5 & 6 = %d\n", 5 & 6);
	printf("5 ^ 6 = %d\n", 5 ^ 6);
	
	printf("val is: %f\n", val);//print val
	//if(val == 5)
	
	intVal = int1 - int2;
	printf("Integer subtraction = %d\n",intVal);//Prints Integer subtraction = -2
	
	intVal = int1 * int2;
	printf("Integer multiplication = %d\n",intVal);//Prints Integer multiplication = 15
	
	int1++;
	int2--;
	printf("Post Increment = %d\n",int1);//Prints Post Increment = 4
	printf("Post decrement = %d\n",int2);//Prints post decrement = 4
}
