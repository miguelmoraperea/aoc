#include <fstream>
#include <iostream>
#include <numeric>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::ifstream myfile("input");
    std::string line;

    int current = 0;
    int line_calories = 0;
    int max_calories = 0;

    while (std::getline(myfile, line)) {
        std::istringstream iss(line);

        if (!(iss >> line_calories)) {
            max_calories = std::max(max_calories, current);
            current = 0;
            continue;
        }

        current += line_calories;
    }

    std::cout << "Max calories = " << max_calories << std::endl;
    return 0;
}
