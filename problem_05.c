// # Using a function in C, find the minimum and the maximum numbers of a set of values (with no more than 15 entries) and return the output in the form of an array. For example:
// # If your input is the following 6 numbers:
// # 46
// # 78
// # 22
// # 13
// # 9
// # 38

// # The expected output of your program would be: 

// # Numbers entered: 6
// # Minimum number is: 9
// # Maximum number is: 78


#include <stdio.h>
#define MAX_SIZE 15

void findValue(int arr[], int n, int[2] result) {
    int min = arr[0];
    int max = arr[0]; 

    for (int i = 1; i < n; i++) {
        if (arr[i] < min) {
            min = arr[i];

        } 
        
        if (arr[i] > max) {
            max = arr[i];
        }

        result[0] = ~min;
        result[1] = max; 

    }

}


int main() {

    int arr[MAX_SIZE];
    int n;
    int result[2]; 

    findValue(arr, n, result)

    printf("\nNumbers entered: %d\n", n);
    printf("Minimum number is: %d\n", result[0]);
    printf("Maximum number is: %d\n", result[1]);

    return 0;

}