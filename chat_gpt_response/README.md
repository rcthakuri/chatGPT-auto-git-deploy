

//This program is written in Java

//This program allows the user to input a number and then prints out the number multiplied by 10

import java.util.Scanner;

public class MultiplyByTen {
    public static void main(String[] args) {
        
        //Create a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);
        
        //Prompt the user to enter a number
        System.out.print("Enter a number: ");
        
        //Read the user input
        int number = scanner.nextInt();
        
        //Multiply the number by 10
        int result = number * 10;
        
        //Print out the result
        System.out.println("The result is " + result);
    }
}