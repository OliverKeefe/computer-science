#include <iostream>
#include <string>

//tools 
const int Pen{ 10 };
const int Marker{ 20 };
const int Eraser{ 30 };

int max;

int a{35};
int b{200};

int main() {
    int tool {Pen};

    switch (tool)
    {
        case Pen : {
            std::cout << "Active tool is Pen" << std::endl;
        }
        break;

        case Marker : {
            std::cout << "Active tool is Marker" << std::endl;
        }
        break;
        case Eraser : {
            std::cout << "Active tool is Eraser" << std::endl;
        }
        break;

    default:
        break;
    }

    auto max = (a > b)? a : 22.5f;

    std::cout << "Max : " << max << std::endl;
}
