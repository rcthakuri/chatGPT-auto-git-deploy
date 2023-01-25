

```java
//This program prints out the first 10 numbers of the Fibonacci sequence
public class Fibonacci {
    public static void main(String[] args) {
        //Declare and initialize the first two numbers of the sequence
        int n1 = 0, n2 = 1, n3;
        System.out.print(n1 + " " + n2); //print out the first two numbers
        
        //Loop through and calculate the next 8 numbers
        for (int i = 2; i < 10; i++) {
            n3 = n1 + n2;
            System.out.print(" " + n3);
            n1 = n2;
            n2 = n3;
        }
    }
}
```