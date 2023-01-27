

//This program is written in C language and it calculates the sum of two numbers

#include<stdio.h>

int main()
{
    //Declaring two variables to store the numbers
    int num1, num2;
    
    //Taking input from the user
    printf("Enter the first number: ");
    scanf("%d", &num1);

    printf("Enter the second number: ");
    scanf("%d", &num2);

    //Calculating the sum of the two numbers
    int sum = num1 + num2;
    
    //Printing the sum
    printf("The sum of the two numbers is %d", sum);

    return 0;
}