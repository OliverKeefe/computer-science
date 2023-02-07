#include <stdio.h>

char buffer[100];

float length1;
float length2;

float width1;
float width2;

float area1;
float area2;

float calculateArea(float length, float width) {
    float area = length * width;
    return area;
}

//float compareArea()

int main() {
    printf("Input your first length: ");
    if (scanf("%f", &length1) != 1) {
        printf("[!] Error: Invalid input.\n");
        
        return 1;
    }
    
    printf("Input your first width: ");
    if (scanf("%f", &width1) != 1) {
        printf("[!] Error: Invalid input.\n");
        
        return 1;
    }

    printf("%f", length1);
    printf("%f", width1);

    printf("Input your second length: ");
    if (scanf("%f", &length2) != 1) {
        printf("[!] Error: Invalid input.\n");
        
        return 1;
    }
    
    printf("Input your second width: ");
    if (scanf("%f", &width2) != 1) {
        printf("[!] Error: Invalid input.\n");
    
        return 1;
    }
    
    printf("%f", length2);
    printf("%f", width2);
    
    area1 = calculateArea(length1, width1); 
    area2 = calculateArea(length2, width2);

    printf("Area1: %f\n", area1);
    printf("Area2: %f\n", area2);

    if (area1 > area2) {
        printf("Area1 is greater.");
    } else if (area1 < area2) {
        printf("Area2 is greater.");
    } else {
        printf("Area1 is equal to Area2.");
    }

    return 0;
}