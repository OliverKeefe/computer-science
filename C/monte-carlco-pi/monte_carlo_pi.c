#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
// !! gcc pi_monte_carlo.c -Werror -lm -o piMonteCarlo  !! (-lm flag fixes the collect2: error: ld returned 1 ext status issue).


/*
Here's an interesting math problem that you can solve in C:

Implement a program to find the value of pi using the Monte Carlo method. The Monte Carlo method is a numerical technique that 
uses random sampling to estimate the value of a mathematical constant or function. In this case, you'll use the Monte Carlo 
method to estimate the value of pi by generating random points in a square and counting the number of points that 
fall within a circle inscribed within the square. The ratio of the number of points within the circle to the total 
umber of points is an estimate of pi/4.

Here's a simple outline of the steps you can follow to implement the Monte Carlo method for finding pi in C:

    1. Initialize a random number generator and set the seed based on the current time to ensure that the random numbers generated are truly random.

    2. Generate a large number of random points (e.g., 100,000) within the square.

    3. For each point, calculate the distance from the center of the circle. If the distance is less than or equal to the radius of the circle, increment a counter that keeps track of the number of points within the circle.

    4. Estimate the value of pi by dividing the count of points within the circle by the total number of points and multiplying by 4.

    5. Repeat the above steps a few times to get an average value for pi.

    6. Compare the estimated value of pi with the actual value (constant M_PI in the math.h library) and print the result.
*/

double max;
double min;
time_t t;

double random_number_generator(double max, double min) {
    double range = (max - min);
    double div = RAND_MAX / range;
    return min + (rand() / div);
}

int main() {
    srand((unsigned) time(&t));
    double real_pi = 3.141593;
    double difference;
    int inCircle = 0;
    int num_points = 100000;
    double pi;

    for (int i = 0; i < num_points; i++) {
        double x = random_number_generator(-1.0, 1.0);
        double y = random_number_generator(-1.0, 1.0);
    
        double distance = sqrt(x * x + y * y);
        if (distance <= 1.0) {
            inCircle++;
        }
    
    }

    // double *ptr = (double*)malloc(150 * sizeof(double));
    // int index = 0;
    // while (index < 150) {
    //     double myRand = random_number_generator(-10000.0, 10000.0);
    //     *(ptr + index) = myRand;
    //     index++;
    // }

    // for (int i = 0; i < 150; i++) {
    //     printf("ptr[%d] = %f\n", i, *(ptr + i));
    // }
    
    pi = 4.0 * (double)inCircle / (double)num_points;
    difference = real_pi - pi;
    printf("Estimated value of pi: %f\n", pi);
    printf("Actual value of pi to 6 decimal places is: %f\n", real_pi);
    printf("Difference is: %f\n", difference);

    return 0;
}