#include <stdio.h>

int main()

{
	int index;
	int arr[][3] = {{1,2,3},{3,4,5},{6,7,8}};//create array ?rowsx3columns which becomes 3x3 given the varaibles
	//1,2,3
	//3,4,5
	//6,7,8
	//refered to by: x[A][B] where 'A' is the row number and ‘B’ is the column
	char array[][3] = {{"hello world"}, {"we will"}, {"rock u"}};// ?x3 rows, which becomes 11 char long
	//hello world
	//we will
	//rock u
	
	for(index = 0; index < 3; index++)
	{
		printf("%s", array[index]);
		printf("%d", arr[index]);//arr[index][]
	}
	
	
return(0);
}
