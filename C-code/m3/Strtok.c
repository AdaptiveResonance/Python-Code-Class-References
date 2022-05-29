#include <string.h>
#include <stdio.h>

int main () {
   char str[20] = "18936ktkfyHelloWorld";
   const char c[2] = "H";
   char *token;
   
   token = strtok(str, c);//returns a pointer to the first token found in the string
   
   /* walk through other tokens */
   while( token != NULL ) {
      printf( " %s\n", token );
    
      token = strtok(NULL, c);
   }
   
   return(0);
}