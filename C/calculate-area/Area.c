/*
Python3 code:

def calc_area(l, w):
    a = l * w
    return a

def main():

    length = int(input("Input Length: "))
    width = int(input("Input Width: "))

    print("Area is: ", calc_area(length,width))

if __name__ == "__main__":
    main() 
*/

#include <stdio.h>

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
    scanf("%f", &length1);
    printf("Input your first width: ");
    scanf("%f", &width1);
    printf("%f", length1);
    printf("%f", width1);

    printf("Input your second length: ");
    scanf("%f", &length2);
    printf("Input your second width: ");
    scanf("%f", &width2);
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