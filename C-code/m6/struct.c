#include<stdio.h>
struct person
{
    char first[16]; // firstname field
    char last[16];  // last field
    int age;        // age field
    char mi;        // middle initial field
};
void printgetit(struct person sia)
{
    printf("Sizeof: %ld\n", sizeof(sia));

 

    printf("printit first is: %s\n", sia.first);
    printf("printit last is: %s\n", sia.last);    
    printf("printit age is: %d\n", sia.age);    
    printf("printit mi is: %c\n", sia.mi);
    printf("Change first name: ");
    scanf("%s", sia.first);
}
void printgetit2(struct person *siaptr)
{
    printf("Sizeof: %ld\n", sizeof(siaptr));
    // 
    printf("printit first is: %s\n", siaptr->first);//-> deference and access siaptr.first
    printf("printit last is: %s\n", siaptr->last);    
    printf("printit age is: %d\n", siaptr->age);    
    printf("printit mi is: %c\n", siaptr->mi);
    printf("Change first name: ");
    scanf("%s", siaptr->first); // this is the same as using "->" (*siaptr).first
}

 

int main()
{
    // in order to access the individual fields of a struct you have to use '.' operator
    // Dot operator say is access the member of this struct.
    //   sia.first[1] is the 2nd charcter of the first member of sia
    //   sia.last[0] is the 1st character of the second member of sia 
    struct person sia = {"Sia", "Lastname", 25, 'M'};
    //printgetit(sia); // passing address of sia to printit
    //printf("In main: printit first is: %s\n", sia.first);
    
    printgetit2(&sia); // passing address of sia to printit
    printf("In main: printit first is: %s\n", sia.first);
    return(0);
}
